#Write functions that can execute the procedures for descriptive and inferential statisitcs
#Overtime, I hope this file may be expanded to perform all basic level statistical operations


#Using the accumulator algorithm, this function returns the mean average by iterating 'score' input to add to 'total'   
def mean(number_of_scores):
        total = 0                                             #initialize counter variable, 'total', to 0
        
        for data in range(number_of_scores):                  #iterate data entry for the number of scores in data set
            score = float(input("Enter score:"))
            total = total + score                             #add each score to accumulate a 'total'
                          
        average = total / number_of_scores                    #obtain 'average' by dividing 'total' by the number of scores in set
        return average
                         




#main function organizes all steps for statistic procedure
def main():
        n = int(input("Enter number of scores in the data set:"))
        print("Mean average of all scores:",mean(n))         #Print the mean average 


#Invoke all steps through the main function
main()
