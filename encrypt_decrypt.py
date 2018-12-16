

print ("                                                                       ")
print ("                                                                       ")
print ("            #####################################################" )       
print ("            #                                                   #" )        
print ("            #                   Caesar Cipher                   #" ) 
print ("            #                                                   #" )                          
print ("            #             Encryption && Decryption Tool         #" )        
print ("            #                                                   #" )        
print ("            #                    Version 1.0                    #" )        
print ("            #                                                   #" )       
print ("            #            Author : Mohin Paramasivam             #" )       
print ("            #                                                   #" )       
print ("            #    Disclaimer : This Algorithm Is Crackable,      #" )
print ("            #                 Use Stronger Algorithm For        #" )
print ("            #                 Classified Communication !!       #" )
print ("            #                                                   #")
print ("            #####################################################" )       

print("                                                                   ")


print("                                           ")



process = input("Please select Encryption or Decryption ( E / D ) : ")

if(process=="Encryption" or process=="ENCRYPTION" or process=="encryption" or process=="E" or process=="e"):


  print("")
  print("")
  mode = input("Please enter encryption mode 'Auto' or 'Manual' ( A / M )  :  ")

  if(mode=="manual" or mode=="M" or mode=="MANUAL" or mode=="Manual" or mode=="m"):
    print("")
    print("")
    shift = int(input("Please enter number of shift ( 0-26 ) : "))

    print("")
    print("")
                                                                                  


    plaintext = input("Enter value to be Encrypted : ")

    print("")
    print("")

    word_type = input("Please enter output type Lowercase or Uppercase ( L or U ) : ")

    print("")

    print("   ")
    print("     ")

    print(" Plaintext : \t\t\t\t\t\t\t" + "Ciphertext : ")
    print("   ")



    length = len(plaintext)

    ##Counter used to point location of plain_text in word

    counter = 0

    """get the plain_text from the input one by one and convert to number form"""

    while(counter!=length):
      plain_text = plaintext[counter].lower()
  
      if(plain_text=="a"):
        value = 1

      elif(plain_text=="b"):
        value = 2

      elif(plain_text=="c"):
        value = 3

      elif(plain_text=="d"):
        value = 4

      elif(plain_text=="e"):
        value = 5

      elif(plain_text=="f"):
        value = 6

      elif(plain_text=="g"):
        value = 7

      elif(plain_text=="h"):
        value = 8

      elif(plain_text=="i"):
        value = 9

      elif(plain_text=="j"):
        value = 10

      elif(plain_text=="k"):
        value = 11

      elif(plain_text=="l"):
        value = 12

      elif(plain_text=="m"):
        value = 13

      elif(plain_text=="n"):
        value = 14

      elif(plain_text=="o"):
        value = 15

      elif(plain_text=="p"):
        value = 16

      elif(plain_text=="q"):
        value = 17

      elif(plain_text=="r"):
        value = 18

      elif(plain_text=="s"):
        value = 19

      elif(plain_text=="t"):
        value = 20

      elif(plain_text=="u"):
        value = 21

      elif(plain_text=="v"):
        value = 22

      elif(plain_text=="w"):
        value = 23

      elif(plain_text=="x"):
        value = 24

      elif(plain_text=="y"):
        value = 25

      elif(plain_text=="z"):
        value = 26

      elif(plain_text=="A"):
        value = 27

      elif(plain_text=="B"):
        value = 28

      elif(plain_text=="C"):
        value = 29

      elif(plain_text=="D"):
        value = 30

      elif(plain_text=="E"):
        value = 31

      elif(plain_text=="F"):
        value = 32

      elif(plain_text=="G"):
        value = 33

      elif(plain_text=="H"):
        value = 34

      elif(plain_text=="I"):
        value = 35

      elif(plain_text=="J"):
        value = 36

      elif(plain_text=="K"):
        value = 37

      elif(plain_text=="L"):
        value = 38

      elif(plain_text=="M"):
        value = 39

      elif(plain_text=="N"):
        value = 40

      elif(plain_text=="O"):
        value = 41

      elif(plain_text=="P"):
        value = 42

      elif(plain_text=="Q"):
        value = 43

      elif(plain_text=="R"):
        value = 44

      elif(plain_text=="S"):
        value = 45

      elif(plain_text=="T"):
        value = 46

      elif(plain_text=="U"):
        value = 47

      elif(plain_text=="V"):
        value = 48

      elif(plain_text=="W"):
        value = 49

      elif(plain_text=="X"):
        value = 50

      elif(plain_text=="Y"):
        value = 51

      elif(plain_text=="Z"):
        value = 52

      else:
        value = -(shift)


        """Ciphertext number after addition operation"""

      plain_text_number = value + shift


      if(plain_text_number==0):
        ciphertext = plaintext[counter]

      elif(plain_text_number==1):
        ciphertext = "a"

      elif(plain_text_number==2):
        ciphertext = "b"

      elif(plain_text_number==3):
        ciphertext = "c"

      elif(plain_text_number==4):
        ciphertext = "d"

      elif(plain_text_number==5):
        ciphertext = "e"

      elif(plain_text_number==6):
        ciphertext = "f"

      elif(plain_text_number==7):
        ciphertext = "g"

      elif(plain_text_number==8):
        ciphertext = "h"

      elif(plain_text_number==9):
        ciphertext = "i"

      elif(plain_text_number==10):
        ciphertext = "j"

      elif(plain_text_number==11):
        ciphertext = "k"

      elif(plain_text_number==12):
        ciphertext = "l"

      elif(plain_text_number==13):
        ciphertext = "m"

      elif(plain_text_number==14):
        ciphertext = "n"

      elif(plain_text_number==15):
        ciphertext = "o"

      elif(plain_text_number==16):
        ciphertext = "p"

      elif(plain_text_number==17):
        ciphertext = "q"

      elif(plain_text_number==18):
        ciphertext = "r"

      elif(plain_text_number==19):
        ciphertext = "s"

      elif(plain_text_number==20):
        ciphertext = "t"

      elif(plain_text_number==21):
        ciphertext = "u"

      elif(plain_text_number==22):
        ciphertext = "v"

      elif(plain_text_number==23):
        ciphertext = "w"

      elif(plain_text_number==24):
        ciphertext = "x"

      elif(plain_text_number==25):
        ciphertext = "y"

      elif(plain_text_number==26):
        ciphertext = "z"

      elif(plain_text_number==27):
        ciphertext = "A"

      elif(plain_text_number==28):
        ciphertext = "B"

      elif(plain_text_number==29):
        ciphertext = "C"

      elif(plain_text_number==30):
        ciphertext = "D"

      elif(plain_text_number==31):
        ciphertext = "E"

      elif(plain_text_number==32):
        ciphertext = "F"

      elif(plain_text_number==33):
        ciphertext = "G"

      elif(plain_text_number==34):
        ciphertext = "H"

      elif(plain_text_number==35):
        ciphertext = "I"

      elif(plain_text_number==36):
        ciphertext = "J"

      elif(plain_text_number==37):
        ciphertext = "K"

      elif(plain_text_number==38):
        ciphertext = "L"

      elif(plain_text_number==39):
        ciphertext = "M"

      elif(plain_text_number==40):
        ciphertext = "N"

      elif(plain_text_number==41):
        ciphertext = "O"

      elif(plain_text_number==42):
        ciphertext = "P"

      elif(plain_text_number==43):
        ciphertext = "Q"

      elif(plain_text_number==44):
        ciphertext = "R"

      elif(plain_text_number==45):
        ciphertext = "S"

      elif(plain_text_number==46):
        ciphertext = "T"

      elif(plain_text_number==47):
        ciphertext = "U"

      elif(plain_text_number==48):
        ciphertext = "V"

      elif(plain_text_number==49):
        ciphertext = "W"

      elif(plain_text_number==50):
        ciphertext = "X"

      elif(plain_text_number==51):
        ciphertext = "Y"

      elif(plain_text_number==52):
        ciphertext = "Z"

  



      if(word_type=="lowercase" or word_type=="l" or word_type=="LOWERCASE" or word_type=="Lowercase" or word_type=="L"):
    
        print("\t"+plain_text.lower()+"\t\t\t\t\t\t\t\t\t\t"+ciphertext.lower())
        counter = counter+1

      elif(word_type=="uppercase" or word_type=="u" or word_type=="UPPERCASE" or word_type=="Uppercase" or word_type=="U"):
    
        print("\t"+plain_text.upper()+"\t\t\t\t\t\t\t\t\t\t"+ciphertext.upper())
        counter = counter+1


  elif(mode=="auto" or mode=="A" or mode=="AUTO" or mode=="Auto" or mode=="a"):
    """Auto mode of 24 shifts"""

    auto_shift = 0;

    print("     ")
    print("     ")

    ciphertext = input("Enter value to be Encrypted : ")

    print("")
    print("")

    word_type = input("Please enter output type Lowercase or Uppercase ( L or U ) : ")
    print("")
    print("   ")
    print("     ")

    while(auto_shift!=25):

      print("")
      print("")

      print(" Plaintext :          ( shift = "+str(auto_shift)+" )"+"\t\t Ciphertext : ")

      print("   ")
  
      length = len(ciphertext)
      counter = 0
      """get the cipher_text from the input one by one and convert to number form"""
      while(counter!=length):
        cipher_text = ciphertext[counter].lower()
    
        if(cipher_text=="a"):
          value = 1
      
        elif(cipher_text=="b"):
          value = 2
      
        elif(cipher_text=="c"):
          value = 3
    
        elif(cipher_text=="d"):
          value = 4

        elif(cipher_text=="e"):
          value = 5

        elif(cipher_text=="f"):
          value = 6

        elif(cipher_text=="g"):
          value = 7

        elif(cipher_text=="h"):
          value = 8

        elif(cipher_text=="i"):
          value = 9

        elif(cipher_text=="j"):
          value = 10

        elif(cipher_text=="k"):
          value = 11

        elif(cipher_text=="l"):
          value = 12

        elif(cipher_text=="m"):
          value = 13

        elif(cipher_text=="n"):
          value = 14

        elif(cipher_text=="o"):
          value = 15

        elif(cipher_text=="p"):
          value = 16

        elif(cipher_text=="q"):
          value = 17

        elif(cipher_text=="r"):
          value = 18

        elif(cipher_text=="s"):
          value = 19

        elif(cipher_text=="t"):
          value = 20

        elif(cipher_text=="u"):
          value = 21

        elif(cipher_text=="v"):
          value = 22

        elif(cipher_text=="w"):
          value = 23

        elif(cipher_text=="x"):
          value = 24

        elif(cipher_text=="y"):
          value = 25

        elif(cipher_text=="z"):
          value = 26

        elif(cipher_text=="A"):
          value = 27

        elif(cipher_text=="B"):
          value = 28

        elif(cipher_text=="C"):
          value = 29

        elif(cipher_text=="D"):
          value = 30

        elif(cipher_text=="E"):
          value = 31

        elif(cipher_text=="F"):
          value = 32

        elif(cipher_text=="G"):
          value = 33

        elif(cipher_text=="H"):
          value = 34

        elif(cipher_text=="I"):
          value = 35

        elif(cipher_text=="J"):
          value = 36

        elif(cipher_text=="K"):
          value = 37

        elif(cipher_text=="L"):
          value = 38

        elif(cipher_text=="M"):
          value = 39

        elif(cipher_text=="N"):
          value = 40

        elif(cipher_text=="O"):
          value = 41

        elif(cipher_text=="P"):
          value = 42

        elif(cipher_text=="Q"):
          value = 43

        elif(cipher_text=="R"):
          value = 44

        elif(cipher_text=="S"):
          value = 45

        elif(cipher_text=="T"):
          value = 46

        elif(cipher_text=="U"):
          value = 47

        elif(cipher_text=="V"):
          value = 48

        elif(cipher_text=="W"):
          value = 49

        elif(cipher_text=="X"):
          value = 50

        elif(cipher_text=="Y"):
          value = 51

        elif(cipher_text=="Z"):
          value = 52

        else:
          value = -auto_shift


        """Plaintext number after substraction operation"""
    
        plain_text_number = value + auto_shift


        if(plain_text_number==0):
          plaintext = ciphertext[counter]

        elif(plain_text_number==1):
          plaintext = "a"

        elif(plain_text_number==2):
          plaintext = "b"

        elif(plain_text_number==3):
          plaintext = "c"

        elif(plain_text_number==4):
          plaintext = "d"

        elif(plain_text_number==5):
          plaintext = "e"

        elif(plain_text_number==6):
          plaintext = "f"

        elif(plain_text_number==7):
          plaintext = "g"

        elif(plain_text_number==8):
          plaintext = "h"

        elif(plain_text_number==9):
          plaintext = "i"

        elif(plain_text_number==10):
          plaintext = "j"

        elif(plain_text_number==11):
          plaintext = "k"

        elif(plain_text_number==12):
          plaintext = "l"

        elif(plain_text_number==13):
          plaintext = "m"

        elif(plain_text_number==14):
          plaintext = "n"

        elif(plain_text_number==15):
          plaintext = "o"

        elif(plain_text_number==16):
          plaintext = "p"

        elif(plain_text_number==17):
          plaintext = "q"

        elif(plain_text_number==18):
          plaintext = "r"

        elif(plain_text_number==19):
          plaintext = "s"

        elif(plain_text_number==20):
          plaintext = "t"

        elif(plain_text_number==21):
          plaintext = "u"

        elif(plain_text_number==22):
          plaintext = "v"

        elif(plain_text_number==23):
          plaintext = "w"

        elif(plain_text_number==24):
          plaintext = "x"

        elif(plain_text_number==25):
          plaintext = "y"

        elif(plain_text_number==26):
          plaintext = "z"

        elif(plain_text_number==27):
          plaintext = "A"

        elif(plain_text_number==28):
          plaintext = "B"

        elif(plain_text_number==29):
          plaintext = "C"

        elif(plain_text_number==30):
          plaintext = "D"

        elif(plain_text_number==31):
          plaintext = "E"

        elif(plain_text_number==32):
          plaintext = "F"

        elif(plain_text_number==33):
          plaintext = "G"

        elif(plain_text_number==34):
          plaintext = "H"

        elif(plain_text_number==35):
          plaintext = "I"

        elif(plain_text_number==36):
          plaintext = "J"

        elif(plain_text_number==37):
          plaintext = "K"

        elif(plain_text_number==38):
          plaintext = "L"

        elif(plain_text_number==39):
          plaintext = "M"

        elif(plain_text_number==40):
          plaintext = "N"

        elif(plain_text_number==41):
          plaintext = "O"

        elif(plain_text_number==42):
          plaintext = "P"

        elif(plain_text_number==43):
          plaintext = "Q"

        elif(plain_text_number==44):
          plaintext = "R"

        elif(plain_text_number==45):
          plaintext = "S"

        elif(plain_text_number==46):
          plaintext = "T"

        elif(plain_text_number==47):
          plaintext = "U"

        elif(plain_text_number==48):
          plaintext = "V"

        elif(plain_text_number==49):
          plaintext = "W"

        elif(plain_text_number==50):
          plaintext = "X"

        elif(plain_text_number==51):
          plaintext = "Y"

        elif(plain_text_number==52):
          plaintext = "Z"

  



        if(word_type=="lowercase" or word_type=="l" or word_type=="LOWERCASE" or word_type=="Lowercase" or word_type=="L"):
          print("\t"+cipher_text.lower()+"\t\t\t\t\t\t\t\t\t\t\t"+plaintext.lower())
          counter = counter+1

        elif(word_type=="uppercase" or word_type=="u" or word_type=="UPPERCASE" or word_type=="Uppercase" or word_type=="U"):
      
          print("\t"+cipher_text.upper()+"\t\t\t\t\t\t\t\t\t\t\t"+plaintext.upper())
          counter = counter+1

    
      auto_shift = auto_shift+1

elif(process=="Decryption" or process=="DECRYPTION" or process=="decryption" or process=="D" or process=="d"):
  print("")
  print("")
  mode = input("Please enter Decryption mode"+ " 'Bruteforce' or 'Manual' ( B / M ) : ")

  if(mode=="Manual" or mode=="M" or mode=="MANUAL" or mode=="manual" or mode=="m"):
    print("")
    print("")
    shift = int(input("Please enter number of Shift ( 0-26 ) : "))
    print("")
    print("")
    ciphertext = input("Enter value to be Decrypted : ")
    print("")
    print("")
    word_type = input("Please enter output type Lowercase or Uppercase ( L or U ) : ")
    print("")
    print("   ")
    print("     ")
    print(" Ciphertext :          ( shift = "+str(shift)+" )"+"\t\t Plaintext : ")
    print("   ")
  
    length = len(ciphertext)
    counter = 0
    """get the cipher_text from the input one by one and convert to number form"""
    while(counter!=length):
      cipher_text = ciphertext[counter].upper()
    
      if(cipher_text=="a"):
        value = 1
      
      elif(cipher_text=="b"):
        value = 2
      
      elif(cipher_text=="c"):
        value = 3
    
      elif(cipher_text=="d"):
        value = 4

      elif(cipher_text=="e"):
        value = 5

      elif(cipher_text=="f"):
        value = 6

      elif(cipher_text=="g"):
        value = 7

      elif(cipher_text=="h"):
        value = 8

      elif(cipher_text=="i"):
        value = 9

      elif(cipher_text=="j"):
        value = 10

      elif(cipher_text=="k"):
        value = 11

      elif(cipher_text=="l"):
        value = 12

      elif(cipher_text=="m"):
        value = 13

      elif(cipher_text=="n"):
        value = 14

      elif(cipher_text=="o"):
        value = 15

      elif(cipher_text=="p"):
        value = 16

      elif(cipher_text=="q"):
        value = 17

      elif(cipher_text=="r"):
        value = 18

      elif(cipher_text=="s"):
        value = 19

      elif(cipher_text=="t"):
        value = 20

      elif(cipher_text=="u"):
        value = 21

      elif(cipher_text=="v"):
        value = 22

      elif(cipher_text=="w"):
        value = 23

      elif(cipher_text=="x"):
        value = 24

      elif(cipher_text=="y"):
        value = 25

      elif(cipher_text=="z"):
        value = 26

      elif(cipher_text=="A"):
        value = 27

      elif(cipher_text=="B"):
        value = 28

      elif(cipher_text=="C"):
        value = 29

      elif(cipher_text=="D"):
        value = 30

      elif(cipher_text=="E"):
        value = 31

      elif(cipher_text=="F"):
        value = 32

      elif(cipher_text=="G"):
        value = 33

      elif(cipher_text=="H"):
        value = 34

      elif(cipher_text=="I"):
        value = 35

      elif(cipher_text=="J"):
        value = 36

      elif(cipher_text=="K"):
        value = 37

      elif(cipher_text=="L"):
        value = 38

      elif(cipher_text=="M"):
        value = 39

      elif(cipher_text=="N"):
        value = 40

      elif(cipher_text=="O"):
        value = 41

      elif(cipher_text=="P"):
        value = 42

      elif(cipher_text=="Q"):
        value = 43

      elif(cipher_text=="R"):
        value = 44

      elif(cipher_text=="S"):
        value = 45

      elif(cipher_text=="T"):
        value = 46

      elif(cipher_text=="U"):
        value = 47

      elif(cipher_text=="V"):
        value = 48

      elif(cipher_text=="W"):
        value = 49

      elif(cipher_text=="X"):
        value = 50

      elif(cipher_text=="Y"):
        value = 51

      elif(cipher_text=="Z"):
        value = 52

      else:
        value = shift


      """Plaintext number after substraction operation"""
    
      plain_text_number = value - shift


      if(plain_text_number==0):
        plaintext = ciphertext[counter]

      elif(plain_text_number==1):
        plaintext = "a"

      elif(plain_text_number==2):
        plaintext = "b"

      elif(plain_text_number==3):
        plaintext = "c"

      elif(plain_text_number==4):
        plaintext = "d"

      elif(plain_text_number==5):
        plaintext = "e"

      elif(plain_text_number==6):
        plaintext = "f"

      elif(plain_text_number==7):
        plaintext = "g"

      elif(plain_text_number==8):
        plaintext = "h"

      elif(plain_text_number==9):
        plaintext = "i"

      elif(plain_text_number==10):
        plaintext = "j"

      elif(plain_text_number==11):
        plaintext = "k"

      elif(plain_text_number==12):
        plaintext = "l"

      elif(plain_text_number==13):
        plaintext = "m"

      elif(plain_text_number==14):
        plaintext = "n"

      elif(plain_text_number==15):
        plaintext = "o"

      elif(plain_text_number==16):
        plaintext = "p"

      elif(plain_text_number==17):
        plaintext = "q"

      elif(plain_text_number==18):
        plaintext = "r"

      elif(plain_text_number==19):
        plaintext = "s"

      elif(plain_text_number==20):
        plaintext = "t"

      elif(plain_text_number==21):
        plaintext = "u"

      elif(plain_text_number==22):
        plaintext = "v"

      elif(plain_text_number==23):
        plaintext = "w"

      elif(plain_text_number==24):
        plaintext = "x"

      elif(plain_text_number==25):
        plaintext = "y"

      elif(plain_text_number==26):
        plaintext = "z"

      elif(plain_text_number==27):
        plaintext = "A"

      elif(plain_text_number==28):
        plaintext = "B"

      elif(plain_text_number==29):
        plaintext = "C"

      elif(plain_text_number==30):
        plaintext = "D"

      elif(plain_text_number==31):
        plaintext = "E"

      elif(plain_text_number==32):
        plaintext = "F"

      elif(plain_text_number==33):
        plaintext = "G"

      elif(plain_text_number==34):
        plaintext = "H"

      elif(plain_text_number==35):
        plaintext = "I"

      elif(plain_text_number==36):
        plaintext = "J"

      elif(plain_text_number==37):
        plaintext = "K"

      elif(plain_text_number==38):
        plaintext = "L"

      elif(plain_text_number==39):
        plaintext = "M"

      elif(plain_text_number==40):
        plaintext = "N"

      elif(plain_text_number==41):
        plaintext = "O"

      elif(plain_text_number==42):
        plaintext = "P"

      elif(plain_text_number==43):
        plaintext = "Q"

      elif(plain_text_number==44):
        plaintext = "R"

      elif(plain_text_number==45):
        plaintext = "S"

      elif(plain_text_number==46):
        plaintext = "T"

      elif(plain_text_number==47):
        plaintext = "U"

      elif(plain_text_number==48):
        plaintext = "V"

      elif(plain_text_number==49):
        plaintext = "W"

      elif(plain_text_number==50):
        plaintext = "X"

      elif(plain_text_number==51):
        plaintext = "Y"

      elif(plain_text_number==52):
        plaintext = "Z"

  



      if(word_type=="lowercase" or word_type=="l" or word_type=="LOWERCASE" or word_type=="L"):
        print("\t"+cipher_text.lower()+"\t\t\t\t\t\t\t\t\t\t\t"+plaintext.lower())
        counter = counter+1

      elif(word_type=="uppercase" or word_type=="u" or word_type=="UPPERCASE" or word_type=="U"):
      
        print("\t"+cipher_text.upper()+"\t\t\t\t\t\t\t\t\t\t\t"+plaintext.upper())
        counter = counter+1

  elif(mode=="Bruteforce" or mode=="B" or mode=="BRUTEFORCE" or mode=="bruteforce" or mode=="b"):

    """Bruteforce mode of 24 shifts"""

    bruteforce_shift = 0;
    print("")
    print("")
    ciphertext = input("Enter value to be Decrypted : ")
    print("")
    print("")
    word_type = input("Please enter output type Lowercase or Uppercase ( L or U ) : ")
    print("")
    print("   ")
    print("     ")

    while(bruteforce_shift!=25):

      print("")
      print("")

      print(" Ciphertext :          ( shift = "+str(bruteforce_shift)+" )"+"\t\t Plaintext : ")

      print("   ")
  
      length = len(ciphertext)
      counter = 0
      """get the cipher_text from the input one by one and convert to number form"""
      while(counter!=length):
        cipher_text = ciphertext[counter].upper()
    
        if(cipher_text=="a"):
          value = 1
      
        elif(cipher_text=="b"):
          value = 2
      
        elif(cipher_text=="c"):
          value = 3
    
        elif(cipher_text=="d"):
          value = 4

        elif(cipher_text=="e"):
          value = 5

        elif(cipher_text=="f"):
          value = 6

        elif(cipher_text=="g"):
          value = 7

        elif(cipher_text=="h"):
          value = 8

        elif(cipher_text=="i"):
          value = 9

        elif(cipher_text=="j"):
          value = 10

        elif(cipher_text=="k"):
          value = 11

        elif(cipher_text=="l"):
          value = 12

        elif(cipher_text=="m"):
          value = 13

        elif(cipher_text=="n"):
          value = 14

        elif(cipher_text=="o"):
          value = 15

        elif(cipher_text=="p"):
          value = 16

        elif(cipher_text=="q"):
          value = 17

        elif(cipher_text=="r"):
          value = 18

        elif(cipher_text=="s"):
          value = 19

        elif(cipher_text=="t"):
          value = 20

        elif(cipher_text=="u"):
          value = 21

        elif(cipher_text=="v"):
          value = 22

        elif(cipher_text=="w"):
          value = 23

        elif(cipher_text=="x"):
          value = 24

        elif(cipher_text=="y"):
          value = 25

        elif(cipher_text=="z"):
          value = 26

        elif(cipher_text=="A"):
          value = 27

        elif(cipher_text=="B"):
          value = 28

        elif(cipher_text=="C"):
          value = 29

        elif(cipher_text=="D"):
          value = 30

        elif(cipher_text=="E"):
          value = 31

        elif(cipher_text=="F"):
          value = 32

        elif(cipher_text=="G"):
          value = 33

        elif(cipher_text=="H"):
          value = 34

        elif(cipher_text=="I"):
          value = 35

        elif(cipher_text=="J"):
          value = 36

        elif(cipher_text=="K"):
          value = 37

        elif(cipher_text=="L"):
          value = 38

        elif(cipher_text=="M"):
          value = 39

        elif(cipher_text=="N"):
          value = 40

        elif(cipher_text=="O"):
          value = 41

        elif(cipher_text=="P"):
          value = 42

        elif(cipher_text=="Q"):
          value = 43

        elif(cipher_text=="R"):
          value = 44

        elif(cipher_text=="S"):
          value = 45

        elif(cipher_text=="T"):
          value = 46

        elif(cipher_text=="U"):
          value = 47

        elif(cipher_text=="V"):
          value = 48

        elif(cipher_text=="W"):
          value = 49

        elif(cipher_text=="X"):
          value = 50

        elif(cipher_text=="Y"):
          value = 51

        elif(cipher_text=="Z"):
          value = 52

        else:
          value = bruteforce_shift


        """Plaintext number after substraction operation"""
    
        plain_text_number = value - bruteforce_shift


        if(plain_text_number==0):
          plaintext = ciphertext[counter]

        elif(plain_text_number==1):
          plaintext = "a"

        elif(plain_text_number==2):
          plaintext = "b"

        elif(plain_text_number==3):
          plaintext = "c"

        elif(plain_text_number==4):
          plaintext = "d"

        elif(plain_text_number==5):
          plaintext = "e"

        elif(plain_text_number==6):
          plaintext = "f"

        elif(plain_text_number==7):
          plaintext = "g"

        elif(plain_text_number==8):
          plaintext = "h"

        elif(plain_text_number==9):
          plaintext = "i"

        elif(plain_text_number==10):
          plaintext = "j"

        elif(plain_text_number==11):
          plaintext = "k"

        elif(plain_text_number==12):
          plaintext = "l"

        elif(plain_text_number==13):
          plaintext = "m"

        elif(plain_text_number==14):
          plaintext = "n"

        elif(plain_text_number==15):
          plaintext = "o"

        elif(plain_text_number==16):
          plaintext = "p"

        elif(plain_text_number==17):
          plaintext = "q"

        elif(plain_text_number==18):
          plaintext = "r"

        elif(plain_text_number==19):
          plaintext = "s"

        elif(plain_text_number==20):
          plaintext = "t"

        elif(plain_text_number==21):
          plaintext = "u"

        elif(plain_text_number==22):
          plaintext = "v"

        elif(plain_text_number==23):
          plaintext = "w"

        elif(plain_text_number==24):
          plaintext = "x"

        elif(plain_text_number==25):
          plaintext = "y"

        elif(plain_text_number==26):
          plaintext = "z"

        elif(plain_text_number==27):
          plaintext = "A"

        elif(plain_text_number==28):
          plaintext = "B"

        elif(plain_text_number==29):
          plaintext = "C"

        elif(plain_text_number==30):
          plaintext = "D"

        elif(plain_text_number==31):
          plaintext = "E"

        elif(plain_text_number==32):
          plaintext = "F"

        elif(plain_text_number==33):
          plaintext = "G"

        elif(plain_text_number==34):
          plaintext = "H"

        elif(plain_text_number==35):
          plaintext = "I"

        elif(plain_text_number==36):
          plaintext = "J"

        elif(plain_text_number==37):
          plaintext = "K"

        elif(plain_text_number==38):
         plaintext = "L"

        elif(plain_text_number==39):
          plaintext = "M"

        elif(plain_text_number==40):
          plaintext = "N"

        elif(plain_text_number==41):
          plaintext = "O"

        elif(plain_text_number==42):
          plaintext = "P"

        elif(plain_text_number==43):
          plaintext = "Q"

        elif(plain_text_number==44):
          plaintext = "R"

        elif(plain_text_number==45):
          plaintext = "S"

        elif(plain_text_number==46):
          plaintext = "T"

        elif(plain_text_number==47):
          plaintext = "U"

        elif(plain_text_number==48):
          plaintext = "V"

        elif(plain_text_number==49):
          plaintext = "W"

        elif(plain_text_number==50):
          plaintext = "X"

        elif(plain_text_number==51):
          plaintext = "Y"

        elif(plain_text_number==52):
          plaintext = "Z"

  



        if(word_type=="lowercase" or word_type=="l" or word_type=="LOWERCASE" or word_type=="L"):
          print("\t"+cipher_text.lower()+"\t\t\t\t\t\t\t\t\t\t\t"+plaintext.lower())
        
          counter = counter+1
        

        elif(word_type=="uppercase" or word_type=="u" or word_type=="UPPERCASE" or word_type=="Uppercase" or word_type=="U"):
          print("\t"+cipher_text.upper()+"\t\t\t\t\t\t\t\t\t\t\t"+plaintext.upper())
      
          counter = counter+1
        
      bruteforce_shift = bruteforce_shift+1


else:

  print("")
  print("Please enter a Valid Mode!!")

  



    







