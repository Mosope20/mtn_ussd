# landing response
first_dict = {
        "1." : "Data Plans",
        "2." : "Social Bundles",
        "3." : "Balance Check",
        "4." : "Roaming/Int\'L",
        "5." : "Borrow Credit/Recharge",
        "6." : "Gift Data",
        "7." : "Video Packs",
        "8." : "Hot Deals"
    }
#------------------------------------------------------------------------------------------------------------------------------------------------
                                                    # option (1) from first_dict
BuyData = {
        "1." : "Daily",
        "2." : "Weekly",
        "3." : "Monthly",
        "4." : "2-3 Month",
        "5." : "Always ON Plans",
        "6." : "Broadband Plans",
        "7." : "Family Packs",
        "8." : "Hot Deals",
        "9." : "5G Plans",
        "10." : "FREE Youtube",
        "11." : "Manage Data",
        "0." : "Back"
    }

# option (1) from BuyData
Daily = {
        "1." : "N50 for 40MB",
        "2." : "N100 for 100MB",
        "3." : "N100 for 350MB(IG/TIKTOK/Youtube)",
        "4." : "N200 for 200MB(3 days)",
        "5." : "N300 for 1GB",
        "6." : "N500 for 2GB(2 days)",
        "7." : "N25 for 250MB (Nightlife)",
        "8." : "N50 for 500MB (Nightlife)",
        "9." : "N300 for 750MB(3-day plan)",
        "10." : "N25 for WhatsApp Daily",
        "11." : "N50 Jolly Combo Offer",
        "12.": "N100 Jolly Combo Offer"
    }














SocialBundle= {
        "1." : "Whatsapp",
        "2." : "Facebook",
        "3." : "Instagram",
        "4." : "Tiktok",
        "5." : "Always ON Plans",
        "99." : "Next",
        "0." : "Back"
    }




dial = input("Dial:> ")

if dial == "*131#":
    for x, y in first_dict.items():
        print(x,y)

reply = int(input("Reply: "))
if reply == 1:
    for x, y in BuyData.items():
        print(x, y)
if reply  == 2:
    for x, y in SocialBundle.items():
        print(x, y)



reply = int(input("Reply: "))
if reply == 0:
    for x, y in first_dict.items():
        print(x,y)

reply = int(input("Reply: "))



if reply == "d":
    exit()