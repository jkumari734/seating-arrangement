# seating-arrangement
## Run Code
	1. Store all .py files and .txt required for execution and testing in one directory. (Python 3.6 and higher required )
	2. Go to that directory in cmd prompt.
	3. On cmd, give two arguments, one main file and second test file for executing the code.
	   E.g,  main.py  test.txt
	4. The command prompt will execute the program and display the path of the output file.
	5. The output file contains all request no.s with respective seats booked.

## Assumptions
	1. All requests will be collected and are fetched in a file together. So the input is not fed into algorithm one by one.
	2. File will have correct inputs, no bad input. 
	3. Files will be given in txt format.
	4. All requests are treated equally regardless of their order.
	5. Theatre utilization is maximum no of seats booked.
	6. Requests which can be processed fully are considered, no partial requests.
	7. Customer satisfaction is highest when all seats for a particular reservation are booked contiguously.
	8. Customer satisfaction has a second factor depending on which seat the user occupies, seats closer to screen are less preferred than seats at the back of theatre and seats more centered in a row is preferred compared to corner seats. All of this constitutes a small weightage to the algorithm.
	9. Final solution is first maximizing the theatre utilization and then togetherness factor for a reservation. Lastly, giving a weightage to seat location for each customer.
	
