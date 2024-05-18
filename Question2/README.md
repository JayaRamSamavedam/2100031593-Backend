### **Question 2. Find all orders placed in January 2023.**
Query:<br>
```sql
SELECT * FROM Orders
WHERE MONTH(OrderDate)=1 AND YEAR(OrderDate)=2023;
```
<br>

![SqlQueryOutput.png](SqlQueryOutput.png)

![PythonCodeOutput.png](PythonCodeOutput.png)
