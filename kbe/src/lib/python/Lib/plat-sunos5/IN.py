# Generated by h2py from /usr/include/netinet/in.h

# Included from sys/feature_tests.h

# Included from sys/isa_defs.h
_CHAR_ALIGNMENT = 1
_SHORT_ALIGNMENT = 2
_INT_ALIGNMENT = 4
_LONG_ALIGNMENT = 8
_LONG_LONG_ALIGNMENT = 8
_DOUBLE_ALIGNMENT = 8
_LONG_DOUBLE_ALIGNMENT = 16
_POINTER_ALIGNMENT = 8
_MAX_ALIGNMENT = 16
_ALIGNMENT_REQUIRED = 1
_CHAR_ALIGNMENT = 1
_SHORT_ALIGNMENT = 2
_INT_ALIGNMENT = 4
_LONG_ALIGNMENT = 4
_LONG_LONG_ALIGNMENT = 4
_DOUBLE_ALIGNMENT = 4
_LONG_DOUBLE_ALIGNMENT = 4
_POINTER_ALIGNMENT = 4
_MAX_ALIGNMENT = 4
_ALIGNMENT_REQUIRED = 0
_CHAR_ALIGNMENT = 1
_SHORT_ALIGNMENT = 2
_INT_ALIGNMENT = 4
_LONG_LONG_ALIGNMENT = 8
_DOUBLE_ALIGNMENT = 8
_ALIGNMENT_REQUIRED = 1
_LONG_ALIGNMENT = 4
_LONG_DOUBLE_ALIGNMENT = 8
_POINTER_ALIGNMENT = 4
_MAX_ALIGNMENT = 8
_LONG_ALIGNMENT = 8
_LONG_DOUBLE_ALIGNMENT = 16
_POINTER_ALIGNMENT = 8
_MAX_ALIGNMENT = 16
_POSIX_C_SOURCE = 1
_LARGEFILE64_SOURCE = 1
_LARGEFILE_SOURCE = 1
_FILE_OFFSET_BITS = 64
_FILE_OFFSET_BITS = 32
_POSIX_C_SOURCE = 199506
_POSIX_PTHREAD_SEMANTICS = 1
_XOPEN_VERSION = 500
_XOPEN_VERSION = 4
_XOPEN_VERSION = 3
from TYPES import *

# Included from sys/stream.h

# Included from sys/vnode.h
from TYPES import *

# Included from sys/t_lock.h

# Included from sys/machlock.h
from TYPES import *
LOCK_HELD_VALUE = 0xff
def SPIN_LOCK(pl): return ((pl) > ipltospl(LOCK_LEVEL))

def LOCK_SAMPLE_INTERVAL(i): return (((i) & 0xff) == 0)

CLOCK_LEVEL = 10
LOCK_LEVEL = 10
DISP_LEVEL = (LOCK_LEVEL + 1)
PTR24_LSB = 5
PTR24_MSB = (PTR24_LSB + 24)
PTR24_ALIGN = 32
PTR24_BASE = 0xe0000000

# Included from sys/param.h
from TYPES import *
_POSIX_VDISABLE = 0
MAX_INPUT = 512
MAX_CANON = 256
UID_NOBODY = 60001
GID_NOBODY = UID_NOBODY
UID_NOACCESS = 60002
MAX_TASKID = 999999
MAX_MAXPID = 999999
DEFAULT_MAXPID = 999999
DEFAULT_JUMPPID = 100000
DEFAULT_MAXPID = 30000
DEFAULT_JUMPPID = 0
MAXUID = 2147483647
MAXPROJID = MAXUID
MAXLINK = 32767
NMOUNT = 40
CANBSIZ = 256
NOFILE = 20
NGROUPS_UMIN = 0
NGROUPS_UMAX = 32
NGROUPS_MAX_DEFAULT = 16
NZERO = 20
NULL = 0
NULL = 0
CMASK = 0o22
CDLIMIT = (1<<11)
NBPS = 0x20000
NBPSCTR = 512
UBSIZE = 512
SCTRSHFT = 9
SYSNAME = 9
PREMOTE = 39
MAXPATHLEN = 1024
MAXSYMLINKS = 20
MAXNAMELEN = 256
NADDR = 13
PIPE_BUF = 5120
PIPE_MAX = 5120
NBBY = 8
MAXBSIZE = 8192
DEV_BSIZE = 512
DEV_BSHIFT = 9
MAXFRAG = 8
MAXOFF32_T = 0x7fffffff
MAXOFF_T = 0x7fffffffffffffff
MAXOFFSET_T = 0x7fffffffffffffff
MAXOFF_T = 0x7fffffff
MAXOFFSET_T = 0x7fffffff
def btodb(bytes): return   \

def dbtob(db): return   \

def lbtodb(bytes): return   \

def ldbtob(db): return   \

NCARGS32 = 0x100000
NCARGS64 = 0x200000
NCARGS = NCARGS64
NCARGS = NCARGS32
FSHIFT = 8
FSCALE = (1<<FSHIFT)
def DELAY(n): return drv_usecwait(n)

def mmu_ptob(x): return ((x) << MMU_PAGESHIFT)

def mmu_btop(x): return (((x)) >> MMU_PAGESHIFT)

def mmu_btopr(x): return ((((x) + MMU_PAGEOFFSET) >> MMU_PAGESHIFT))

def mmu_ptod(x): return ((x) << (MMU_PAGESHIFT - DEV_BSHIFT))

def ptod(x): return ((x) << (PAGESHIFT - DEV_BSHIFT))

def ptob(x): return ((x) << PAGESHIFT)

def btop(x): return (((x) >> PAGESHIFT))

def btopr(x): return ((((x) + PAGEOFFSET) >> PAGESHIFT))

def dtop(DD): return (((DD) + NDPP - 1) >> (PAGESHIFT - DEV_BSHIFT))

def dtopt(DD): return ((DD) >> (PAGESHIFT - DEV_BSHIFT))

_AIO_LISTIO_MAX = (4096)
_AIO_MAX = (-1)
_MQ_OPEN_MAX = (32)
_MQ_PRIO_MAX = (32)
_SEM_NSEMS_MAX = INT_MAX
_SEM_VALUE_MAX = INT_MAX

# Included from sys/unistd.h
_CS_PATH = 65
_CS_LFS_CFLAGS = 68
_CS_LFS_LDFLAGS = 69
_CS_LFS_LIBS = 70
_CS_LFS_LINTFLAGS = 71
_CS_LFS64_CFLAGS = 72
_CS_LFS64_LDFLAGS = 73
_CS_LFS64_LIBS = 74
_CS_LFS64_LINTFLAGS = 75
_CS_XBS5_ILP32_OFF32_CFLAGS = 700
_CS_XBS5_ILP32_OFF32_LDFLAGS = 701
_CS_XBS5_ILP32_OFF32_LIBS = 702
_CS_XBS5_ILP32_OFF32_LINTFLAGS = 703
_CS_XBS5_ILP32_OFFBIG_CFLAGS = 705
_CS_XBS5_ILP32_OFFBIG_LDFLAGS = 706
_CS_XBS5_ILP32_OFFBIG_LIBS = 707
_CS_XBS5_ILP32_OFFBIG_LINTFLAGS = 708
_CS_XBS5_LP64_OFF64_CFLAGS = 709
_CS_XBS5_LP64_OFF64_LDFLAGS = 710
_CS_XBS5_LP64_OFF64_LIBS = 711
_CS_XBS5_LP64_OFF64_LINTFLAGS = 712
_CS_XBS5_LPBIG_OFFBIG_CFLAGS = 713
_CS_XBS5_LPBIG_OFFBIG_LDFLAGS = 714
_CS_XBS5_LPBIG_OFFBIG_LIBS = 715
_CS_XBS5_LPBIG_OFFBIG_LINTFLAGS = 716
_SC_ARG_MAX = 1
_SC_CHILD_MAX = 2
_SC_CLK_TCK = 3
_SC_NGROUPS_MAX = 4
_SC_OPEN_MAX = 5
_SC_JOB_CONTROL = 6
_SC_SAVED_IDS = 7
_SC_VERSION = 8
_SC_PASS_MAX = 9
_SC_LOGNAME_MAX = 10
_SC_PAGESIZE = 11
_SC_XOPEN_VERSION = 12
_SC_NPROCESSORS_CONF = 14
_SC_NPROCESSORS_ONLN = 15
_SC_STREAM_MAX = 16
_SC_TZNAME_MAX = 17
_SC_AIO_LISTIO_MAX = 18
_SC_AIO_MAX = 19
_SC_AIO_PRIO_DELTA_MAX = 20
_SC_ASYNCHRONOUS_IO = 21
_SC_DELAYTIMER_MAX = 22
_SC_FSYNC = 23
_SC_MAPPED_FILES = 24
_SC_MEMLOCK = 25
_SC_MEMLOCK_RANGE = 26
_SC_MEMORY_PROTECTION = 27
_SC_MESSAGE_PASSING = 28
_SC_MQ_OPEN_MAX = 29
_SC_MQ_PRIO_MAX = 30
_SC_PRIORITIZED_IO = 31
_SC_PRIORITY_SCHEDULING = 32
_SC_REALTIME_SIGNALS = 33
_SC_RTSIG_MAX = 34
_SC_SEMAPHORES = 35
_SC_SEM_NSEMS_MAX = 36
_SC_SEM_VALUE_MAX = 37
_SC_SHARED_MEMORY_OBJECTS = 38
_SC_SIGQUEUE_MAX = 39
_SC_SIGRT_MIN = 40
_SC_SIGRT_MAX = 41
_SC_SYNCHRONIZED_IO = 42
_SC_TIMERS = 43
_SC_TIMER_MAX = 44
_SC_2_C_BIND = 45
_SC_2_C_DEV = 46
_SC_2_C_VERSION = 47
_SC_2_FORT_DEV = 48
_SC_2_FORT_RUN = 49
_SC_2_LOCALEDEF = 50
_SC_2_SW_DEV = 51
_SC_2_UPE = 52
_SC_2_VERSION = 53
_SC_BC_BASE_MAX = 54
_SC_BC_DIM_MAX = 55
_SC_BC_SCALE_MAX = 56
_SC_BC_STRING_MAX = 57
_SC_COLL_WEIGHTS_MAX = 58
_SC_EXPR_NEST_MAX = 59
_SC_LINE_MAX = 60
_SC_RE_DUP_MAX = 61
_SC_XOPEN_CRYPT = 62
_SC_XOPEN_ENH_I18N = 63
_SC_XOPEN_SHM = 64
_SC_2_CHAR_TERM = 66
_SC_XOPEN_XCU_VERSION = 67
_SC_ATEXIT_MAX = 76
_SC_IOV_MAX = 77
_SC_XOPEN_UNIX = 78
_SC_PAGE_SIZE = _SC_PAGESIZE
_SC_T_IOV_MAX = 79
_SC_PHYS_PAGES = 500
_SC_AVPHYS_PAGES = 501
_SC_COHER_BLKSZ = 503
_SC_SPLIT_CACHE = 504
_SC_ICACHE_SZ = 505
_SC_DCACHE_SZ = 506
_SC_ICACHE_LINESZ = 507
_SC_DCACHE_LINESZ = 508
_SC_ICACHE_BLKSZ = 509
_SC_DCACHE_BLKSZ = 510
_SC_DCACHE_TBLKSZ = 511
_SC_ICACHE_ASSOC = 512
_SC_DCACHE_ASSOC = 513
_SC_MAXPID = 514
_SC_STACK_PROT = 515
_SC_THREAD_DESTRUCTOR_ITERATIONS = 568
_SC_GETGR_R_SIZE_MAX = 569
_SC_GETPW_R_SIZE_MAX = 570
_SC_LOGIN_NAME_MAX = 571
_SC_THREAD_KEYS_MAX = 572
_SC_THREAD_STACK_MIN = 573
_SC_THREAD_THREADS_MAX = 574
_SC_TTY_NAME_MAX = 575
_SC_THREADS = 576
_SC_THREAD_ATTR_STACKADDR = 577
_SC_THREAD_ATTR_STACKSIZE = 578
_SC_THREAD_PRIORITY_SCHEDULING = 579
_SC_THREAD_PRIO_INHERIT = 580
_SC_THREAD_PRIO_PROTECT = 581
_SC_THREAD_PROCESS_SHARED = 582
_SC_THREAD_SAFE_FUNCTIONS = 583
_SC_XOPEN_LEGACY = 717
_SC_XOPEN_REALTIME = 718
_SC_XOPEN_REALTIME_THREADS = 719
_SC_XBS5_ILP32_OFF32 = 720
_SC_XBS5_ILP32_OFFBIG = 721
_SC_XBS5_LP64_OFF64 = 722
_SC_XBS5_LPBIG_OFFBIG = 723
_PC_LINK_MAX = 1
_PC_MAX_CANON = 2
_PC_MAX_INPUT = 3
_PC_NAME_MAX = 4
_PC_PATH_MAX = 5
_PC_PIPE_BUF = 6
_PC_NO_TRUNC = 7
_PC_VDISABLE = 8
_PC_CHOWN_RESTRICTED = 9
_PC_ASYNC_IO = 10
_PC_PRIO_IO = 11
_PC_SYNC_IO = 12
_PC_FILESIZEBITS = 67
_PC_LAST = 67
_POSIX_VERSION = 199506
_POSIX2_VERSION = 199209
_POSIX2_C_VERSION = 199209
_XOPEN_XCU_VERSION = 4
_XOPEN_REALTIME = 1
_XOPEN_ENH_I18N = 1
_XOPEN_SHM = 1
_POSIX2_C_BIND = 1
_POSIX2_CHAR_TERM = 1
_POSIX2_LOCALEDEF = 1
_POSIX2_C_DEV = 1
_POSIX2_SW_DEV = 1
_POSIX2_UPE = 1

# Included from sys/mutex.h
from TYPES import *
def MUTEX_HELD(x): return (mutex_owned(x))


# Included from sys/rwlock.h
from TYPES import *
def RW_READ_HELD(x): return (rw_read_held((x)))

def RW_WRITE_HELD(x): return (rw_write_held((x)))

def RW_LOCK_HELD(x): return (rw_lock_held((x)))

def RW_ISWRITER(x): return (rw_iswriter(x))


# Included from sys/semaphore.h

# Included from sys/thread.h
from TYPES import *

# Included from sys/klwp.h
from TYPES import *

# Included from sys/condvar.h
from TYPES import *

# Included from sys/time.h

# Included from sys/types32.h

# Included from sys/int_types.h
TIME32_MAX = INT32_MAX
TIME32_MIN = INT32_MIN
def TIMEVAL_OVERFLOW(tv): return \

from TYPES import *
DST_NONE = 0
DST_USA = 1
DST_AUST = 2
DST_WET = 3
DST_MET = 4
DST_EET = 5
DST_CAN = 6
DST_GB = 7
DST_RUM = 8
DST_TUR = 9
DST_AUSTALT = 10
ITIMER_REAL = 0
ITIMER_VIRTUAL = 1
ITIMER_PROF = 2
ITIMER_REALPROF = 3
def ITIMERVAL_OVERFLOW(itv): return \

SEC = 1
MILLISEC = 1000
MICROSEC = 1000000
NANOSEC = 1000000000

# Included from sys/time_impl.h
def TIMESPEC_OVERFLOW(ts): return \

def ITIMERSPEC_OVERFLOW(it): return \

__CLOCK_REALTIME0 = 0
CLOCK_VIRTUAL = 1
CLOCK_PROF = 2
__CLOCK_REALTIME3 = 3
CLOCK_HIGHRES = 4
CLOCK_MAX = 5
CLOCK_REALTIME = __CLOCK_REALTIME3
CLOCK_REALTIME = __CLOCK_REALTIME0
TIMER_RELTIME = 0x0
TIMER_ABSTIME = 0x1
def TICK_TO_SEC(tick): return ((tick) / hz)

def SEC_TO_TICK(sec): return ((sec) * hz)

def TICK_TO_MSEC(tick): return \

def MSEC_TO_TICK(msec): return \

def MSEC_TO_TICK_ROUNDUP(msec): return \

def TICK_TO_USEC(tick): return ((tick) * usec_per_tick)

def USEC_TO_TICK(usec): return ((usec) / usec_per_tick)

def USEC_TO_TICK_ROUNDUP(usec): return \

def TICK_TO_NSEC(tick): return ((tick) * nsec_per_tick)

def NSEC_TO_TICK(nsec): return ((nsec) / nsec_per_tick)

def NSEC_TO_TICK_ROUNDUP(nsec): return \

def TIMEVAL_TO_TICK(tvp): return \

def TIMESTRUC_TO_TICK(tsp): return \


# Included from time.h
from TYPES import *

# Included from iso/time_iso.h
NULL = 0
NULL = 0
CLOCKS_PER_SEC = 1000000

# Included from sys/select.h
FD_SETSIZE = 65536
FD_SETSIZE = 1024
_NBBY = 8
NBBY = _NBBY
def FD_ZERO(p): return bzero((p), sizeof (*(p)))


# Included from sys/signal.h

# Included from sys/iso/signal_iso.h
SIGHUP = 1
SIGINT = 2
SIGQUIT = 3
SIGILL = 4
SIGTRAP = 5
SIGIOT = 6
SIGABRT = 6
SIGEMT = 7
SIGFPE = 8
SIGKILL = 9
SIGBUS = 10
SIGSEGV = 11
SIGSYS = 12
SIGPIPE = 13
SIGALRM = 14
SIGTERM = 15
SIGUSR1 = 16
SIGUSR2 = 17
SIGCLD = 18
SIGCHLD = 18
SIGPWR = 19
SIGWINCH = 20
SIGURG = 21
SIGPOLL = 22
SIGIO = SIGPOLL
SIGSTOP = 23
SIGTSTP = 24
SIGCONT = 25
SIGTTIN = 26
SIGTTOU = 27
SIGVTALRM = 28
SIGPROF = 29
SIGXCPU = 30
SIGXFSZ = 31
SIGWAITING = 32
SIGLWP = 33
SIGFREEZE = 34
SIGTHAW = 35
SIGCANCEL = 36
SIGLOST = 37
_SIGRTMIN = 38
_SIGRTMAX = 45
SIG_BLOCK = 1
SIG_UNBLOCK = 2
SIG_SETMASK = 3
SIGNO_MASK = 0xFF
SIGDEFER = 0x100
SIGHOLD = 0x200
SIGRELSE = 0x400
SIGIGNORE = 0x800
SIGPAUSE = 0x1000

# Included from sys/siginfo.h
from TYPES import *
SIGEV_NONE = 1
SIGEV_SIGNAL = 2
SIGEV_THREAD = 3
SI_NOINFO = 32767
SI_USER = 0
SI_LWP = (-1)
SI_QUEUE = (-2)
SI_TIMER = (-3)
SI_ASYNCIO = (-4)
SI_MESGQ = (-5)

# Included from sys/machsig.h
ILL_ILLOPC = 1
ILL_ILLOPN = 2
ILL_ILLADR = 3
ILL_ILLTRP = 4
ILL_PRVOPC = 5
ILL_PRVREG = 6
ILL_COPROC = 7
ILL_BADSTK = 8
NSIGILL = 8
EMT_TAGOVF = 1
EMT_CPCOVF = 2
NSIGEMT = 2
FPE_INTDIV = 1
FPE_INTOVF = 2
FPE_FLTDIV = 3
FPE_FLTOVF = 4
FPE_FLTUND = 5
FPE_FLTRES = 6
FPE_FLTINV = 7
FPE_FLTSUB = 8
NSIGFPE = 8
SEGV_MAPERR = 1
SEGV_ACCERR = 2
NSIGSEGV = 2
BUS_ADRALN = 1
BUS_ADRERR = 2
BUS_OBJERR = 3
NSIGBUS = 3
TRAP_BRKPT = 1
TRAP_TRACE = 2
TRAP_RWATCH = 3
TRAP_WWATCH = 4
TRAP_XWATCH = 5
NSIGTRAP = 5
CLD_EXITED = 1
CLD_KILLED = 2
CLD_DUMPED = 3
CLD_TRAPPED = 4
CLD_STOPPED = 5
CLD_CONTINUED = 6
NSIGCLD = 6
POLL_IN = 1
POLL_OUT = 2
POLL_MSG = 3
POLL_ERR = 4
POLL_PRI = 5
POLL_HUP = 6
NSIGPOLL = 6
PROF_SIG = 1
NSIGPROF = 1
SI_MAXSZ = 256
SI_MAXSZ = 128

# Included from sys/time_std_impl.h
from TYPES import *
SI32_MAXSZ = 128
def SI_CANQUEUE(c): return ((c) <= SI_QUEUE)

SA_NOCLDSTOP = 0x00020000
SA_ONSTACK = 0x00000001
SA_RESETHAND = 0x00000002
SA_RESTART = 0x00000004
SA_SIGINFO = 0x00000008
SA_NODEFER = 0x00000010
SA_NOCLDWAIT = 0x00010000
SA_WAITSIG = 0x00010000
NSIG = 46
MAXSIG = 45
S_SIGNAL = 1
S_SIGSET = 2
S_SIGACTION = 3
S_NONE = 4
MINSIGSTKSZ = 2048
SIGSTKSZ = 8192
SS_ONSTACK = 0x00000001
SS_DISABLE = 0x00000002
SN_PROC = 1
SN_CANCEL = 2
SN_SEND = 3

# Included from sys/ucontext.h
from TYPES import *

# Included from sys/regset.h
REG_CCR = (0)
REG_PSR = (0)
REG_PSR = (0)
REG_PC = (1)
REG_nPC = (2)
REG_Y = (3)
REG_G1 = (4)
REG_G2 = (5)
REG_G3 = (6)
REG_G4 = (7)
REG_G5 = (8)
REG_G6 = (9)
REG_G7 = (10)
REG_O0 = (11)
REG_O1 = (12)
REG_O2 = (13)
REG_O3 = (14)
REG_O4 = (15)
REG_O5 = (16)
REG_O6 = (17)
REG_O7 = (18)
REG_ASI = (19)
REG_FPRS = (20)
REG_PS = REG_PSR
REG_SP = REG_O6
REG_R0 = REG_O0
REG_R1 = REG_O1
_NGREG = 21
_NGREG = 19
NGREG = _NGREG
_NGREG32 = 19
_NGREG64 = 21
SPARC_MAXREGWINDOW = 31
MAXFPQ = 16
XRS_ID = 0x78727300

# Included from v7/sys/privregs.h

# Included from v7/sys/psr.h
PSR_CWP = 0x0000001F
PSR_ET = 0x00000020
PSR_PS = 0x00000040
PSR_S = 0x00000080
PSR_PIL = 0x00000F00
PSR_EF = 0x00001000
PSR_EC = 0x00002000
PSR_RSV = 0x000FC000
PSR_ICC = 0x00F00000
PSR_C = 0x00100000
PSR_V = 0x00200000
PSR_Z = 0x00400000
PSR_N = 0x00800000
PSR_VER = 0x0F000000
PSR_IMPL = 0xF0000000
PSL_ALLCC = PSR_ICC
PSL_USER = (PSR_S)
PSL_USERMASK = (PSR_ICC)
PSL_UBITS = (PSR_ICC|PSR_EF)
def USERMODE(ps): return (((ps) & PSR_PS) == 0)


# Included from sys/fsr.h
FSR_CEXC = 0x0000001f
FSR_AEXC = 0x000003e0
FSR_FCC = 0x00000c00
FSR_PR = 0x00001000
FSR_QNE = 0x00002000
FSR_FTT = 0x0001c000
FSR_VER = 0x000e0000
FSR_TEM = 0x0f800000
FSR_RP = 0x30000000
FSR_RD = 0xc0000000
FSR_VER_SHIFT = 17
FSR_FCC1 = 0x00000003
FSR_FCC2 = 0x0000000C
FSR_FCC3 = 0x00000030
FSR_CEXC_NX = 0x00000001
FSR_CEXC_DZ = 0x00000002
FSR_CEXC_UF = 0x00000004
FSR_CEXC_OF = 0x00000008
FSR_CEXC_NV = 0x00000010
FSR_AEXC_NX = (0x1 << 5)
FSR_AEXC_DZ = (0x2 << 5)
FSR_AEXC_UF = (0x4 << 5)
FSR_AEXC_OF = (0x8 << 5)
FSR_AEXC_NV = (0x10 << 5)
FTT_NONE = 0
FTT_IEEE = 1
FTT_UNFIN = 2
FTT_UNIMP = 3
FTT_SEQ = 4
FTT_ALIGN = 5
FTT_DFAULT = 6
FSR_FTT_SHIFT = 14
FSR_FTT_IEEE = (FTT_IEEE   << FSR_FTT_SHIFT)
FSR_FTT_UNFIN = (FTT_UNFIN  << FSR_FTT_SHIFT)
FSR_FTT_UNIMP = (FTT_UNIMP  << FSR_FTT_SHIFT)
FSR_FTT_SEQ = (FTT_SEQ    << FSR_FTT_SHIFT)
FSR_FTT_ALIGN = (FTT_ALIGN  << FSR_FTT_SHIFT)
FSR_FTT_DFAULT = (FTT_DFAULT << FSR_FTT_SHIFT)
FSR_TEM_NX = (0x1 << 23)
FSR_TEM_DZ = (0x2 << 23)
FSR_TEM_UF = (0x4 << 23)
FSR_TEM_OF = (0x8 << 23)
FSR_TEM_NV = (0x10 << 23)
RP_DBLEXT = 0
RP_SINGLE = 1
RP_DOUBLE = 2
RP_RESERVED = 3
RD_NEAR = 0
RD_ZER0 = 1
RD_POSINF = 2
RD_NEGINF = 3
FPRS_DL = 0x1
FPRS_DU = 0x2
FPRS_FEF = 0x4
PIL_MAX = 0xf
def SAVE_GLOBALS(RP): return \

def RESTORE_GLOBALS(RP): return \

def SAVE_OUTS(RP): return \

def RESTORE_OUTS(RP): return \

def SAVE_WINDOW(SBP): return \

def RESTORE_WINDOW(SBP): return \

def STORE_FPREGS(FP): return \

def LOAD_FPREGS(FP): return \

_SPARC_MAXREGWINDOW = 31
_XRS_ID = 0x78727300
GETCONTEXT = 0
SETCONTEXT = 1
UC_SIGMASK = 0o01
UC_STACK = 0o02
UC_CPU = 0o04
UC_MAU = 0o10
UC_FPU = UC_MAU
UC_INTR = 0o20
UC_ASR = 0o40
UC_MCONTEXT = (UC_CPU|UC_FPU|UC_ASR)
UC_ALL = (UC_SIGMASK|UC_STACK|UC_MCONTEXT)
_SIGQUEUE_MAX = 32
_SIGNOTIFY_MAX = 32

# Included from sys/pcb.h
INSTR_VALID = 0x02
NORMAL_STEP = 0x04
WATCH_STEP = 0x08
CPC_OVERFLOW = 0x10
ASYNC_HWERR = 0x20
STEP_NONE = 0
STEP_REQUESTED = 1
STEP_ACTIVE = 2
STEP_WASACTIVE = 3

# Included from sys/msacct.h
LMS_USER = 0
LMS_SYSTEM = 1
LMS_TRAP = 2
LMS_TFAULT = 3
LMS_DFAULT = 4
LMS_KFAULT = 5
LMS_USER_LOCK = 6
LMS_SLEEP = 7
LMS_WAIT_CPU = 8
LMS_STOPPED = 9
NMSTATES = 10

# Included from sys/lwp.h

# Included from sys/synch.h
from TYPES import *
USYNC_THREAD = 0x00
USYNC_PROCESS = 0x01
LOCK_NORMAL = 0x00
LOCK_ERRORCHECK = 0x02
LOCK_RECURSIVE = 0x04
USYNC_PROCESS_ROBUST = 0x08
LOCK_PRIO_NONE = 0x00
LOCK_PRIO_INHERIT = 0x10
LOCK_PRIO_PROTECT = 0x20
LOCK_STALL_NP = 0x00
LOCK_ROBUST_NP = 0x40
LOCK_OWNERDEAD = 0x1
LOCK_NOTRECOVERABLE = 0x2
LOCK_INITED = 0x4
LOCK_UNMAPPED = 0x8
LWP_DETACHED = 0x00000040
LWP_SUSPENDED = 0x00000080
__LWP_ASLWP = 0x00000100
MAXSYSARGS = 8
NORMALRETURN = 0
JUSTRETURN = 1
LWP_USER = 0x01
LWP_SYS = 0x02
TS_FREE = 0x00
TS_SLEEP = 0x01
TS_RUN = 0x02
TS_ONPROC = 0x04
TS_ZOMB = 0x08
TS_STOPPED = 0x10
T_INTR_THREAD = 0x0001
T_WAKEABLE = 0x0002
T_TOMASK = 0x0004
T_TALLOCSTK = 0x0008
T_WOULDBLOCK = 0x0020
T_DONTBLOCK = 0x0040
T_DONTPEND = 0x0080
T_SYS_PROF = 0x0100
T_WAITCVSEM = 0x0200
T_WATCHPT = 0x0400
T_PANIC = 0x0800
TP_HOLDLWP = 0x0002
TP_TWAIT = 0x0004
TP_LWPEXIT = 0x0008
TP_PRSTOP = 0x0010
TP_CHKPT = 0x0020
TP_EXITLWP = 0x0040
TP_PRVSTOP = 0x0080
TP_MSACCT = 0x0100
TP_STOPPING = 0x0200
TP_WATCHPT = 0x0400
TP_PAUSE = 0x0800
TP_CHANGEBIND = 0x1000
TS_LOAD = 0x0001
TS_DONT_SWAP = 0x0002
TS_SWAPENQ = 0x0004
TS_ON_SWAPQ = 0x0008
TS_CSTART = 0x0100
TS_UNPAUSE = 0x0200
TS_XSTART = 0x0400
TS_PSTART = 0x0800
TS_RESUME = 0x1000
TS_CREATE = 0x2000
TS_ALLSTART = \
        (TS_CSTART|TS_UNPAUSE|TS_XSTART|TS_PSTART|TS_RESUME|TS_CREATE)
def CPR_VSTOPPED(t): return \

def THREAD_TRANSITION(tp): return thread_transition(tp);

def THREAD_STOP(tp): return \

def THREAD_ZOMB(tp): return THREAD_SET_STATE(tp, TS_ZOMB, NULL)

def SEMA_HELD(x): return (sema_held((x)))

NO_LOCKS_HELD = 1
NO_COMPETING_THREADS = 1

# Included from sys/cred.h

# Included from sys/uio.h
from TYPES import *

# Included from sys/resource.h
from TYPES import *
PRIO_PROCESS = 0
PRIO_PGRP = 1
PRIO_USER = 2
RLIMIT_CPU = 0
RLIMIT_FSIZE = 1
RLIMIT_DATA = 2
RLIMIT_STACK = 3
RLIMIT_CORE = 4
RLIMIT_NOFILE = 5
RLIMIT_VMEM = 6
RLIMIT_AS = RLIMIT_VMEM
RLIM_NLIMITS = 7
RLIM_INFINITY = (-3)
RLIM_SAVED_MAX = (-2)
RLIM_SAVED_CUR = (-1)
RLIM_INFINITY = 0x7fffffff
RLIM_SAVED_MAX = 0x7ffffffe
RLIM_SAVED_CUR = 0x7ffffffd
RLIM32_INFINITY = 0x7fffffff
RLIM32_SAVED_MAX = 0x7ffffffe
RLIM32_SAVED_CUR = 0x7ffffffd

# Included from sys/model.h

# Included from sys/debug.h
def ASSERT64(x): return ASSERT(x)

def ASSERT32(x): return ASSERT(x)

DATAMODEL_MASK = 0x0FF00000
DATAMODEL_ILP32 = 0x00100000
DATAMODEL_LP64 = 0x00200000
DATAMODEL_NONE = 0
DATAMODEL_NATIVE = DATAMODEL_LP64
DATAMODEL_NATIVE = DATAMODEL_ILP32
def STRUCT_SIZE(handle): return \

def STRUCT_BUF(handle): return ((handle).ptr.m64)

def SIZEOF_PTR(umodel): return \

def STRUCT_SIZE(handle): return (sizeof (*(handle).ptr))

def STRUCT_BUF(handle): return ((handle).ptr)

def SIZEOF_PTR(umodel): return sizeof (caddr_t)

def lwp_getdatamodel(t): return DATAMODEL_ILP32

RUSAGE_SELF = 0
RUSAGE_CHILDREN = -1

# Included from vm/seg_enum.h

# Included from sys/buf.h

# Included from sys/kstat.h
from TYPES import *
KSTAT_STRLEN = 31
def KSTAT_ENTER(k): return \

def KSTAT_EXIT(k): return \

KSTAT_TYPE_RAW = 0
KSTAT_TYPE_NAMED = 1
KSTAT_TYPE_INTR = 2
KSTAT_TYPE_IO = 3
KSTAT_TYPE_TIMER = 4
KSTAT_NUM_TYPES = 5
KSTAT_FLAG_VIRTUAL = 0x01
KSTAT_FLAG_VAR_SIZE = 0x02
KSTAT_FLAG_WRITABLE = 0x04
KSTAT_FLAG_PERSISTENT = 0x08
KSTAT_FLAG_DORMANT = 0x10
KSTAT_FLAG_INVALID = 0x20
KSTAT_READ = 0
KSTAT_WRITE = 1
KSTAT_DATA_CHAR = 0
KSTAT_DATA_INT32 = 1
KSTAT_DATA_UINT32 = 2
KSTAT_DATA_INT64 = 3
KSTAT_DATA_UINT64 = 4
KSTAT_DATA_LONG = KSTAT_DATA_INT32
KSTAT_DATA_ULONG = KSTAT_DATA_UINT32
KSTAT_DATA_LONG = KSTAT_DATA_INT64
KSTAT_DATA_ULONG = KSTAT_DATA_UINT64
KSTAT_DATA_LONG = 7
KSTAT_DATA_ULONG = 8
KSTAT_DATA_LONGLONG = KSTAT_DATA_INT64
KSTAT_DATA_ULONGLONG = KSTAT_DATA_UINT64
KSTAT_DATA_FLOAT = 5
KSTAT_DATA_DOUBLE = 6
KSTAT_INTR_HARD = 0
KSTAT_INTR_SOFT = 1
KSTAT_INTR_WATCHDOG = 2
KSTAT_INTR_SPURIOUS = 3
KSTAT_INTR_MULTSVC = 4
KSTAT_NUM_INTRS = 5
B_BUSY = 0x0001
B_DONE = 0x0002
B_ERROR = 0x0004
B_PAGEIO = 0x0010
B_PHYS = 0x0020
B_READ = 0x0040
B_WRITE = 0x0100
B_KERNBUF = 0x0008
B_WANTED = 0x0080
B_AGE = 0x000200
B_ASYNC = 0x000400
B_DELWRI = 0x000800
B_STALE = 0x001000
B_DONTNEED = 0x002000
B_REMAPPED = 0x004000
B_FREE = 0x008000
B_INVAL = 0x010000
B_FORCE = 0x020000
B_HEAD = 0x040000
B_NOCACHE = 0x080000
B_TRUNC = 0x100000
B_SHADOW = 0x200000
B_RETRYWRI = 0x400000
def notavail(bp): return \

def BWRITE(bp): return \

def BWRITE2(bp): return \

VROOT = 0x01
VNOCACHE = 0x02
VNOMAP = 0x04
VDUP = 0x08
VNOSWAP = 0x10
VNOMOUNT = 0x20
VISSWAP = 0x40
VSWAPLIKE = 0x80
VVFSLOCK = 0x100
VVFSWAIT = 0x200
VVMLOCK = 0x400
VDIROPEN = 0x800
VVMEXEC = 0x1000
VPXFS = 0x2000
AT_TYPE = 0x0001
AT_MODE = 0x0002
AT_UID = 0x0004
AT_GID = 0x0008
AT_FSID = 0x0010
AT_NODEID = 0x0020
AT_NLINK = 0x0040
AT_SIZE = 0x0080
AT_ATIME = 0x0100
AT_MTIME = 0x0200
AT_CTIME = 0x0400
AT_RDEV = 0x0800
AT_BLKSIZE = 0x1000
AT_NBLOCKS = 0x2000
AT_VCODE = 0x4000
AT_ALL = (AT_TYPE|AT_MODE|AT_UID|AT_GID|AT_FSID|AT_NODEID|\
                        AT_NLINK|AT_SIZE|AT_ATIME|AT_MTIME|AT_CTIME|\
                        AT_RDEV|AT_BLKSIZE|AT_NBLOCKS|AT_VCODE)
AT_STAT = (AT_MODE|AT_UID|AT_GID|AT_FSID|AT_NODEID|AT_NLINK|\
                        AT_SIZE|AT_ATIME|AT_MTIME|AT_CTIME|AT_RDEV)
AT_TIMES = (AT_ATIME|AT_MTIME|AT_CTIME)
AT_NOSET = (AT_NLINK|AT_RDEV|AT_FSID|AT_NODEID|AT_TYPE|\
                        AT_BLKSIZE|AT_NBLOCKS|AT_VCODE)
VSUID = 0o4000
VSGID = 0o2000
VSVTX = 0o1000
VREAD = 0o0400
VWRITE = 0o0200
VEXEC = 0o0100
MODEMASK = 0o7777
PERMMASK = 0o0777
def MANDMODE(mode): return (((mode) & (VSGID|(VEXEC>>3))) == VSGID)

VSA_ACL = 0x0001
VSA_ACLCNT = 0x0002
VSA_DFACL = 0x0004
VSA_DFACLCNT = 0x0008
LOOKUP_DIR = 0x01
DUMP_ALLOC = 0
DUMP_FREE = 1
DUMP_SCAN = 2
ATTR_UTIME = 0x01
ATTR_EXEC = 0x02
ATTR_COMM = 0x04
ATTR_HINT = 0x08
ATTR_REAL = 0x10

# Included from sys/poll.h
POLLIN = 0x0001
POLLPRI = 0x0002
POLLOUT = 0x0004
POLLRDNORM = 0x0040
POLLWRNORM = POLLOUT
POLLRDBAND = 0x0080
POLLWRBAND = 0x0100
POLLNORM = POLLRDNORM
POLLERR = 0x0008
POLLHUP = 0x0010
POLLNVAL = 0x0020
POLLREMOVE = 0x0800
POLLRDDATA = 0x0200
POLLNOERR = 0x0400
POLLCLOSED = 0x8000

# Included from sys/strmdep.h
def str_aligned(X): return (((ulong_t)(X) & (sizeof (int) - 1)) == 0)


# Included from sys/strft.h
tdelta_t_sz = 12
FTEV_MASK = 0x1FFF
FTEV_ISWR = 0x8000
FTEV_CS = 0x4000
FTEV_PS = 0x2000
FTEV_QMASK = 0x1F00
FTEV_ALLOCMASK = 0x1FF8
FTEV_ALLOCB = 0x0000
FTEV_ESBALLOC = 0x0001
FTEV_DESBALLOC = 0x0002
FTEV_ESBALLOCA = 0x0003
FTEV_DESBALLOCA = 0x0004
FTEV_ALLOCBIG = 0x0005
FTEV_ALLOCBW = 0x0006
FTEV_FREEB = 0x0008
FTEV_DUPB = 0x0009
FTEV_COPYB = 0x000A
FTEV_CALLER = 0x000F
FTEV_PUT = 0x0100
FTEV_FSYNCQ = 0x0103
FTEV_DSYNCQ = 0x0104
FTEV_PUTQ = 0x0105
FTEV_GETQ = 0x0106
FTEV_RMVQ = 0x0107
FTEV_INSQ = 0x0108
FTEV_PUTBQ = 0x0109
FTEV_FLUSHQ = 0x010A
FTEV_REPLYQ = 0x010B
FTEV_PUTNEXT = 0x010D
FTEV_RWNEXT = 0x010E
FTEV_QWINNER = 0x010F
FTEV_GEWRITE = 0x0101
def FTFLW_HASH(h): return (((unsigned)(h))%ftflw_hash_sz)

FTBLK_EVNTS = 0x9
QENAB = 0x00000001
QWANTR = 0x00000002
QWANTW = 0x00000004
QFULL = 0x00000008
QREADR = 0x00000010
QUSE = 0x00000020
QNOENB = 0x00000040
QBACK = 0x00000100
QHLIST = 0x00000200
QPAIR = 0x00000800
QPERQ = 0x00001000
QPERMOD = 0x00002000
QMTSAFE = 0x00004000
QMTOUTPERIM = 0x00008000
QMT_TYPEMASK = (QPAIR|QPERQ|QPERMOD|QMTSAFE|QMTOUTPERIM)
QINSERVICE = 0x00010000
QWCLOSE = 0x00020000
QEND = 0x00040000
QWANTWSYNC = 0x00080000
QSYNCSTR = 0x00100000
QISDRV = 0x00200000
QHOT = 0x00400000
QNEXTHOT = 0x00800000
_QINSERTING = 0x04000000
_QREMOVING = 0x08000000
Q_SQQUEUED = 0x01
Q_SQDRAINING = 0x02
QB_FULL = 0x01
QB_WANTW = 0x02
QB_BACK = 0x04
NBAND = 256
STRUIOT_NONE = -1
STRUIOT_DONTCARE = 0
STRUIOT_STANDARD = 1
STRUIOT_IP = 2
DBLK_REFMIN = 0x01
STRUIO_SPEC = 0x01
STRUIO_DONE = 0x02
STRUIO_IP = 0x04
STRUIO_ZC = 0x08
STRUIO_ICK = 0x10
MSGMARK = 0x01
MSGNOLOOP = 0x02
MSGDELIM = 0x04
MSGNOGET = 0x08
MSGMARKNEXT = 0x10
MSGNOTMARKNEXT = 0x20
M_DATA = 0x00
M_PROTO = 0x01
M_BREAK = 0x08
M_PASSFP = 0x09
M_EVENT = 0x0a
M_SIG = 0x0b
M_DELAY = 0x0c
M_CTL = 0x0d
M_IOCTL = 0x0e
M_SETOPTS = 0x10
M_RSE = 0x11
M_IOCACK = 0x81
M_IOCNAK = 0x82
M_PCPROTO = 0x83
M_PCSIG = 0x84
M_READ = 0x85
M_FLUSH = 0x86
M_STOP = 0x87
M_START = 0x88
M_HANGUP = 0x89
M_ERROR = 0x8a
M_COPYIN = 0x8b
M_COPYOUT = 0x8c
M_IOCDATA = 0x8d
M_PCRSE = 0x8e
M_STOPI = 0x8f
M_STARTI = 0x90
M_PCEVENT = 0x91
M_UNHANGUP = 0x92
QNORM = 0x00
QPCTL = 0x80
IOC_MODELS = DATAMODEL_MASK
IOC_ILP32 = DATAMODEL_ILP32
IOC_LP64 = DATAMODEL_LP64
IOC_NATIVE = DATAMODEL_NATIVE
IOC_NONE = DATAMODEL_NONE
STRCANON = 0x01
RECOPY = 0x02
SO_ALL = 0x003f
SO_READOPT = 0x0001
SO_WROFF = 0x0002
SO_MINPSZ = 0x0004
SO_MAXPSZ = 0x0008
SO_HIWAT = 0x0010
SO_LOWAT = 0x0020
SO_MREADON = 0x0040
SO_MREADOFF = 0x0080
SO_NDELON = 0x0100
SO_NDELOFF = 0x0200
SO_ISTTY = 0x0400
SO_ISNTTY = 0x0800
SO_TOSTOP = 0x1000
SO_TONSTOP = 0x2000
SO_BAND = 0x4000
SO_DELIM = 0x8000
SO_NODELIM = 0x010000
SO_STRHOLD = 0x020000
SO_ERROPT = 0x040000
SO_COPYOPT = 0x080000
SO_MAXBLK = 0x100000
DEF_IOV_MAX = 16
INFOD_FIRSTBYTES = 0x02
INFOD_BYTES = 0x04
INFOD_COUNT = 0x08
INFOD_COPYOUT = 0x10
MODOPEN = 0x1
CLONEOPEN = 0x2
CONSOPEN = 0x4
OPENFAIL = -1
BPRI_LO = 1
BPRI_MED = 2
BPRI_HI = 3
BPRI_FT = 4
INFPSZ = -1
FLUSHALL = 1
FLUSHDATA = 0
STRHIGH = 5120
STRLOW = 1024
MAXIOCBSZ = 1024
PERIM_INNER = 1
PERIM_OUTER = 2
def datamsg(type): return \

def straln(a): return (caddr_t)((intptr_t)(a) & ~(sizeof (int)-1))


# Included from sys/byteorder.h
def ntohl(x): return (x)

def ntohs(x): return (x)

def htonl(x): return (x)

def htons(x): return (x)

IPPROTO_IP = 0
IPPROTO_HOPOPTS = 0
IPPROTO_ICMP = 1
IPPROTO_IGMP = 2
IPPROTO_GGP = 3
IPPROTO_ENCAP = 4
IPPROTO_TCP = 6
IPPROTO_EGP = 8
IPPROTO_PUP = 12
IPPROTO_UDP = 17
IPPROTO_IDP = 22
IPPROTO_IPV6 = 41
IPPROTO_ROUTING = 43
IPPROTO_FRAGMENT = 44
IPPROTO_RSVP = 46
IPPROTO_ESP = 50
IPPROTO_AH = 51
IPPROTO_ICMPV6 = 58
IPPROTO_NONE = 59
IPPROTO_DSTOPTS = 60
IPPROTO_HELLO = 63
IPPROTO_ND = 77
IPPROTO_EON = 80
IPPROTO_PIM = 103
IPPROTO_RAW = 255
IPPROTO_MAX = 256
IPPORT_ECHO = 7
IPPORT_DISCARD = 9
IPPORT_SYSTAT = 11
IPPORT_DAYTIME = 13
IPPORT_NETSTAT = 15
IPPORT_FTP = 21
IPPORT_TELNET = 23
IPPORT_SMTP = 25
IPPORT_TIMESERVER = 37
IPPORT_NAMESERVER = 42
IPPORT_WHOIS = 43
IPPORT_MTP = 57
IPPORT_BOOTPS = 67
IPPORT_BOOTPC = 68
IPPORT_TFTP = 69
IPPORT_RJE = 77
IPPORT_FINGER = 79
IPPORT_TTYLINK = 87
IPPORT_SUPDUP = 95
IPPORT_EXECSERVER = 512
IPPORT_LOGINSERVER = 513
IPPORT_CMDSERVER = 514
IPPORT_EFSSERVER = 520
IPPORT_BIFFUDP = 512
IPPORT_WHOSERVER = 513
IPPORT_ROUTESERVER = 520
IPPORT_RESERVED = 1024
IPPORT_USERRESERVED = 5000
IMPLINK_IP = 155
IMPLINK_LOWEXPER = 156
IMPLINK_HIGHEXPER = 158
IN_CLASSA_NSHIFT = 24
IN_CLASSA_MAX = 128
IN_CLASSB_NSHIFT = 16
IN_CLASSB_MAX = 65536
IN_CLASSC_NSHIFT = 8
IN_CLASSD_NSHIFT = 28
def IN_MULTICAST(i): return IN_CLASSD(i)

IN_LOOPBACKNET = 127
def IN_SET_LOOPBACK_ADDR(a): return \

def IN6_IS_ADDR_UNSPECIFIED(addr): return \

def IN6_IS_ADDR_LOOPBACK(addr): return \

def IN6_IS_ADDR_LOOPBACK(addr): return \

def IN6_IS_ADDR_MULTICAST(addr): return \

def IN6_IS_ADDR_MULTICAST(addr): return \

def IN6_IS_ADDR_LINKLOCAL(addr): return \

def IN6_IS_ADDR_LINKLOCAL(addr): return \

def IN6_IS_ADDR_SITELOCAL(addr): return \

def IN6_IS_ADDR_SITELOCAL(addr): return \

def IN6_IS_ADDR_V4MAPPED(addr): return \

def IN6_IS_ADDR_V4MAPPED(addr): return \

def IN6_IS_ADDR_V4MAPPED_ANY(addr): return \

def IN6_IS_ADDR_V4MAPPED_ANY(addr): return \

def IN6_IS_ADDR_V4COMPAT(addr): return \

def IN6_IS_ADDR_V4COMPAT(addr): return \

def IN6_IS_ADDR_MC_RESERVED(addr): return \

def IN6_IS_ADDR_MC_RESERVED(addr): return \

def IN6_IS_ADDR_MC_NODELOCAL(addr): return \

def IN6_IS_ADDR_MC_NODELOCAL(addr): return \

def IN6_IS_ADDR_MC_LINKLOCAL(addr): return \

def IN6_IS_ADDR_MC_LINKLOCAL(addr): return \

def IN6_IS_ADDR_MC_SITELOCAL(addr): return \

def IN6_IS_ADDR_MC_SITELOCAL(addr): return \

def IN6_IS_ADDR_MC_ORGLOCAL(addr): return \

def IN6_IS_ADDR_MC_ORGLOCAL(addr): return \

def IN6_IS_ADDR_MC_GLOBAL(addr): return \

def IN6_IS_ADDR_MC_GLOBAL(addr): return \

IP_OPTIONS = 1
IP_HDRINCL = 2
IP_TOS = 3
IP_TTL = 4
IP_RECVOPTS = 5
IP_RECVRETOPTS = 6
IP_RECVDSTADDR = 7
IP_RETOPTS = 8
IP_MULTICAST_IF = 0x10
IP_MULTICAST_TTL = 0x11
IP_MULTICAST_LOOP = 0x12
IP_ADD_MEMBERSHIP = 0x13
IP_DROP_MEMBERSHIP = 0x14
IP_SEC_OPT = 0x22
IPSEC_PREF_NEVER = 0x01
IPSEC_PREF_REQUIRED = 0x02
IPSEC_PREF_UNIQUE = 0x04
IP_ADD_PROXY_ADDR = 0x40
IP_BOUND_IF = 0x41
IP_UNSPEC_SRC = 0x42
IP_REUSEADDR = 0x104
IP_DONTROUTE = 0x105
IP_BROADCAST = 0x106
IP_DEFAULT_MULTICAST_TTL = 1
IP_DEFAULT_MULTICAST_LOOP = 1
IPV6_RTHDR_TYPE_0 = 0
IPV6_UNICAST_HOPS = 0x5
IPV6_MULTICAST_IF = 0x6
IPV6_MULTICAST_HOPS = 0x7
IPV6_MULTICAST_LOOP = 0x8
IPV6_JOIN_GROUP = 0x9
IPV6_LEAVE_GROUP = 0xa
IPV6_ADD_MEMBERSHIP = 0x9
IPV6_DROP_MEMBERSHIP = 0xa
IPV6_PKTINFO = 0xb
IPV6_HOPLIMIT = 0xc
IPV6_NEXTHOP = 0xd
IPV6_HOPOPTS = 0xe
IPV6_DSTOPTS = 0xf
IPV6_RTHDR = 0x10
IPV6_RTHDRDSTOPTS = 0x11
IPV6_RECVPKTINFO = 0x12
IPV6_RECVHOPLIMIT = 0x13
IPV6_RECVHOPOPTS = 0x14
IPV6_RECVDSTOPTS = 0x15
IPV6_RECVRTHDR = 0x16
IPV6_RECVRTHDRDSTOPTS = 0x17
IPV6_CHECKSUM = 0x18
IPV6_BOUND_IF = 0x41
IPV6_UNSPEC_SRC = 0x42
INET_ADDRSTRLEN = 16
INET6_ADDRSTRLEN = 46
IPV6_PAD1_OPT = 0
