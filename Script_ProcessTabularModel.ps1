$timestamp = get-date -f "yyyyMMdd_hhmm"

# Get script name
$ScriptFullPath = $MyInvocation.MyCommand.Path + "_" + $timestamp
# Start logging stdout and stderr to file
Start-Transcript -Path "$ScriptFullPath.log" -Append



[System.Reflection.Assembly]::LoadWithPartialName("Microsoft.AnalysisServices")
[System.Reflection.Assembly]::LoadWithPartialName("Microsoft.AnalysisServices.Core")

$serverName = "azcloudwn002.azure.kp.org"
$databaseName = "HiteshTabular" #HiteshTabular #KomalTabular

$svr = [Microsoft.AnalysisServices.Server]::new()

$svr.Connect($serverName)
$svr.CaptureXml = $true;
$database = $svr.Databases.FindByName($databaseName)
$model = $database.Model
$model.RequestRefresh([Microsoft.AnalysisServices.Tabular.RefreshType]::Full)
$model.SaveChanges()

$resultCollection = [Microsoft.AnalysisServices.XmlaResultCollection]

$resultCollection = $svr.ExecuteCaptureLog($false, $false);

[String]$ErrorMessages = "";

if($resultCollection.ContainsErrors -eq $true){
    $ErrorMessages += "Errors occured in cube {ConnectionString.CatalogName}:  " + $databaseName + "`n"
    foreach ($res in $resultCollection) {
    $obj = $res.Messages
    #Write-Output $obj
        foreach ($Errors in $obj) {
        #Write-Output $Errors
            if ($Errors.GetType() -eq [Microsoft.AnalysisServices.XmlaError]) {
                $ErrorMessages += "ERROR: " +   $Errors.Description + "`n"
                BREAK;
            }
            elseif ($Errors.GetType() -eq [Microsoft.AnalysisServices.XmlaWarning]) {
                $ErrorMessages += "WARNING: " +   $Errors.Description + "`n"
            }
        }
    }
}
else{
    $ErrorMessages += "CUBE PROCESSING SUCCESSFUL" + "`n"
    }

Write-Output $ErrorMessages

$svr.CaptureXml = $false;

$svr.Disconnect()


# Stop logging
Stop-Transcript