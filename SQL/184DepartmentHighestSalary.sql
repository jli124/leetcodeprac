# 184. Deparment Highest Salary
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

/* Sub query and left Join */

#-------------------------------------------------------------------------------
#    Soluton1
#-------------------------------------------------------------------------------
SELECT dep.Name Department,
		em.Name Employee,
		em.Salary Salary
FROM Employee em
LEFT JOIN Department dep
ON em.DepartmentId = dep.Id
WHERE (dep.Id, em.Salary) IN (
	SELECT DepartmentId, MAX(Salary)
	FROM Employee
	GROUP BY DepartmentId
)


;



#-------------------------------------------------------------------------------
#    Soluton2
#-------------------------------------------------------------------------------

