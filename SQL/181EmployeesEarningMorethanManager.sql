# 181. Employees Earning More than their Managers
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

/* Inner Join */

#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------
SELECT em1.Name Employee 
FROM Employee em1
JOIN Employee em2
ON em1.ManagerId = em2.Id 
WHERE em1.Salary > em2.Salary
;


#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------

