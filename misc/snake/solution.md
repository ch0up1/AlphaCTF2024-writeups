
![Screenshot 2024-03-11 114956](https://github.com/ch0up1/AlphaCTF2024-writeups/assets/162801424/3691a802-f51c-4f90-864f-625101334e6e)


Challenge name :  snake🐍

![Screenshot 2024-03-11 115217](https://github.com/ch0up1/AlphaCTF2024-writeups/assets/162801424/cedc1bdb-5451-41e8-8398-dfa706de08c5)


first thing we can see that the script is run in python 2 and from previous knowledge i know that input is vulnerable in python 2 and can execute function in it


from :https://www.geeksforgeeks.org/vulnerability-input-function-python-2-x/ 
![Screenshot 2024-03-11 115621](https://github.com/ch0up1/AlphaCTF2024-writeups/assets/162801424/906ca482-3fcb-4b7c-9c2b-d4136474026c)


we can see in the code that the "inp" variable must :
  -be 3 string length
  -must be bigger than 10e99

so if i pass 
