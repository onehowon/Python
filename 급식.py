import neispy
import asyncio

name = "전남외국어고등학교"

async def main():
    AE = "Q10"
    SE1 = "test001"
    SE2 = "test002"
    neis = neispy.Client()

    scinfo = neis.schoolInfo(SCHUL_NM = 전남외국어고등학교)
    AE = scinfo[0].ATPT_OFCDC_SC_CODE
    SE = scinfo[0].SD_SCHUL_CODE

    scmeal = neis.mealServiceDietInfo(AE,SE, MLSV_YMD=20210604)
    meal = scmeal[0].DDISH_NM.replace("<br/>", "\n")

    scschedule = neis.SchoolSchedule(AE, SE, AA_YMD = 20210604)
    schedule = scschedule[0].EVENT_NM

    sctimetable = neis.timeTable("els", AE, SE, 2019, 2, 20210704, 1, 1)
    timetable = [i.ITRT_CNTNT for i in sectimetable]

    academyinfo = neis.acaInsTiInfo(AE)
    academy = academyinfo[0].ACA_NM

    scclass = neis.classInfo(AE,SE, GRADE=3)
    class_info = [i.CLASS_NM for i in scclass]

    hiscinfo = neis.schoolInfo(SCHUL_NM="전남외국어")
    hAE = hiscinfo[0].ATPT_OFCDC_SC_CODE
    hSE = hiscinfo[0].SD_SCHUL_CODE

    scmajorinfo = neis.schoolMajorinfo(hAE, hSE)
    majorinfo = [m.DDDEP_NM for a in scAflcoinfo]

    sctiClrm = neis.tiClrminfo(hAE, hSE)
    tiClem = [t.CLRM_NM for t in sctiClrm]

    print(AE)
    print(SE)
    print(meal)
    print(schedule)
    print(academy)
    print(class_info)
    print(timetable)
    print(majorinfo)
    print(Aflco)
    print(tiClem)

main()