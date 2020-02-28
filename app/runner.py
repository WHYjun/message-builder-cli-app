# -*- coding: utf-8 -*-
"""
app.runner.py

"""

from module.company import Company
from module.guest import Guest
from module.template import Template
from module.messagebuilder import MessageBuilder
from dotenv import load_dotenv
import os


def run():
    try:
        print("I am here to help you send a message to guest!")
        guest = Guest().initialize_with_user_input()
        company = Company().initialize_with_user_input()
        template = Template().initialize_with_user_input()
        reservation = guest.get_reservation()

        print("Thank you for your input. I am currently generating your message!")
        final_message = MessageBuilder(template).populate_company(
            company).populate_guest(guest).populate_reservation(reservation).build()
        print("Here is your message")
        print(final_message.body)
    except:
        mode = os.getenv("MODE")
        if mode == "PROD":
            print("Restart the program.")
            run()
        if mode == "DEBUG":
            raise


if __name__ == "__main__":
    load_dotenv(verbose=True)
    run()
