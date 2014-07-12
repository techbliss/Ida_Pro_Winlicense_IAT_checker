
import idc
import idaapi

sEA = 0x0000000140001000
eEA = sEA + 0x1
ea = GetEntryPoint(1)
ea2 = MaxEA
idc.LoadDebugger("windbg", 1)
LoadDebugger("windbg", 1)
AddBptEx(0x0000000140001000, 0x1, BPT_BRK)
SetDebuggerOptions(DOPT_BPT_MSGS)
path = GetInputFilePath()
args = ''
sdir = ''
StartDebugger(path, args, sdir)
enable_extlang_python(True)
MakeCode(0x0000000140001000)
PauseProcess()
enable_extlang_python(True)
analyze_area(sEA, eEA)
StopDebugger()



print "##################################################\n" \
      "        What just HAppend your asked ?            \n" \
      "        While you blinked.                        \n" \
      "       IDA Python did the work for you            \n" \
      "                                                  \n" \
      "         WinLicense Easy settings checker       \n" \
      "#############################################\n" \
      " Storm Shadow      \n" \
      "#############################################\n"
print ("IAT = 0000000140001000")
print ("WinLicense IAT is FOUND\n" \
      "IMPORT Breakpoint Adress into Scullahide")
Jump(0x0000000140001000)
