MTN USSD Menu Simulation
This project simulates the MTN USSD menu using Python dictionaries and console input/output. Users can navigate through various menu options such as Data Plans, Social Bundles, Balance Check, and more, simulating the real-life experience of using MTN’s *131# USSD service.

Features
Data Plans: Options for daily, weekly, monthly, multi-month, family packs, and more.
Social Bundles: Access popular social bundles like WhatsApp, Facebook, Instagram, and TikTok.
Balance Check: Check account balances (functionality not implemented yet).
Roaming & International: Roaming data, travel plans, and international calling.
Borrow Credit/Recharge: Options to borrow airtime or data and recharge.
Gift Data: Transfer data to friends, buy data for others, or request data.
Video Packs: Access video packs for platforms like YouTube, Showmax, and StarTimes.
Hot Deals: Special offers and combo packs.
Project Structure
The project is structured using nested dictionaries, where each dictionary represents a menu or submenu with key-value pairs for each option.

first_dict: Main menu options, accessible by dialing *131#.
Submenu dictionaries (e.g., BuyData, SocialBundle, etc.) for each main menu option.
How to Use
Run the Python script.
Enter the USSD code *131# to access the main menu.
Follow the prompts by typing the number of your chosen option (e.g., 1 for Data Plans).
For submenus, type the corresponding number to navigate further or type 0 to go back.
Type d to exit the program at any point.
