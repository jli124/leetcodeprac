# 180. Consecutive Numbers
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

/* Join three tables */

#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------
SELECT DISTINCT(lg1.Num) AS ConsecutiveNums
FROM Logs as lg1, Logs as lg2, Logs as lg3
WHERE lg1.Id + 1 = lg2.Id AND lg2.Id + 1 = lg3.Id 
AND lg1.NUM = lg2.NUM and lg2.NUM = lg3.Num
;


#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------

