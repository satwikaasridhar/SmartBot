from datetime import datetime


addr = ""
def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "sup?",):
        return("Hey! How are you?\n")
        

    if user_message in ("who are you", "who are you?", "help"):
        return "I am Smart Bot.\nI can help you!"

    if user_message in ("time", "time?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time)

    return "Enter \"orderfood\" to order food\nEnter \"menu\" to see the menu\nEnter \"time\" to see the time\nEnter \"address\n[your address]\" to update your address\nEnter \"who are you\" to know more about me!"



def menu():
    return ("Available Items:\n1. Apple: $5\n2. Grape: $3\n3. Orange: $3\n4. StrawBerry: $4\n5. Banana: $2\n\n Enter your order in the format: order\n[serial number of item] [quantity]\n[serial number of item] [quantity]\n...\n[serial number of item] [quantity]\n\nExample:\norder\n1 2\n2 1\n3 1\n\nThis will order 2 Apples, 1 Grape and 1 Orange.")

def address(input_text):
    global addr
    addr = input_text
    return("Your address has been saved as " + addr + "!")

def orderp():
    return "Enter your order in the format: order\n[serial number of item] [quantity]\n[serial number of item] [quantity]\n...\n[serial number of item] [quantity]\n\nExample:\norder\n1 2\n2 1\n3 1\n\nThis will order 2 Apples, 1 Grape and 1 Orange."
    
def order(input_text):
    #return(input_text)
    global addr
    s = ""
    amount = 0
    for i in range(len(input_text)):
        if input_text[i].split()[0] == "1":
            s += "Apple: " + input_text[i].split()[1] + "\n"
            amount += 5 * int(input_text[i].split()[1])
        elif input_text[i].split()[0] == "2":
            s += "Grape: " + input_text[i].split()[1] + "\n"
            amount += 3 * int(input_text[i].split()[1])
        elif input_text[i].split()[0] == "3":
            s += "Orange: " + input_text[i].split()[1] + "\n"
            amount += 3 * int(input_text[i].split()[1])
        elif input_text[i].split()[0] == "4":
            s += "StrawBerry: " + input_text[i].split()[1] + "\n"
            amount += 4 * int(input_text[i].split()[1])
        elif input_text[i].split()[0] == "5":
            s += "Banana: " + input_text[i].split()[1] + "\n"
            amount += 2 * int(input_text[i].split()[1])
    if addr == "":
        return "Enter your address first using. Enter 'address \n [your address]' to update your address"
    return "Your order has been placed!\nYour order is:\n" + s + "Your Order Total: $"+ str(amount) + "\nYour order will be delivered to " + addr + " in 30 minutes."
