# 197. Rising Temperature
/*
Given a weather table write a SQL query to find all dates' id with higher temperature
compared to its previous dates
id | RecordDate (DATE) | Temperature(INT)

Output:
Id

*/
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------
/*
*/


#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------
SELECT w1.Id
FROM weather w1
INNER JOIN weather w2
ON w1.Temperature > w2.Temperature 
AND DATEDIFF(w1.RecordDate, w2.RecordDate) = 1 ;



#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------

