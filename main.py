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
        "12.": "N100 Jolly Combo Offer",
        "0." : "Back"
    }
# option (2) from BuyData
Weekly = {
        "1." : "N200 for 1GB(IG/TIKTOK/Youtube ONLY)",
        "2." : "N300 for 350MB",
        "3." : "N500 for 1.5GB",
        "4." : "N500 for 750MB(2-Week plan)",
        "5." : "N1500 for 6GB",
        "6." : "N1000 for 2GB",
        "7." : "N500 for 1GB",
        "8." : "N50 for WhatsApp Weekly",
        "9." : "N500 for 750MB+1hr YouTube",
        "0." : "Back"
    }
# option (3) from BuyData
Monthly = {
        "1." : "N1,000 for 1.5GB",
        "2." : "N1200 for 2GB",
        "3." : "N1,500 for 3GB",
        "4." : "N2,000 for 4.5GB",
        "5." : "N2,500 for 6GB",
        "6." : "N3,500 for 12GB",
        "7." : "N5,000 for 20GB",
        "8." : "N6,000 for 25GB",
        "9." : "N10,000 for 40GB",
        "10." : "N15,000 for 75GB",
        "11." : "N20,000 for 120GB",
        "12." : "N30,000 for 200GB",
        "13." : "N3,000 for 10GB",
        "0." : "Back"
    }
# option (4) from BuyData
Multi_Month = {
        "1." : "N8,000 for 30GB\\60Days",
        "2." : "N20,000 for 100GB\\60Days",
        "3." : "N30,000 for 160GB\\60Days",
        "4." : "N50,000 for 400GB\\90Days",
        "5." : "N75,000 for 600GB\\90Days",
        "0." : "Back"
        }
# option (5) from BuyData
Always_On = {
        "1." : "N60 for 200MB/24 Hrs",
        "2." : "N120 for 450MB/ 7 Days",
        "3." : "N3000 for 15GB/ 30 Days",
        "4." : "N6000 for 45GB/ 30Days",
        "0." : "Back"
        }
# option (6) from BuyData
Broadband = {
        "1." : "Link Device",
        "2." : "Recharge Device",
        "3." : "Buy Data Bundle on Device",
        "4." : "Check Device Balance",
        "0." : "View & Unlink Device"
        }
# option (7) from BuyData
Family = {
        "1." : "Buy Family Pack",
        "2." : "Add New Beneficiary/Sponsor",
        "3." : "Manage Beneficiary/Sponsor",
        "4." : "Balance Enquiry",
        "5." : "Deactivate Service",
        "6." : "Help",
        "0." : "Back"
        }
# option (8) from BuyData
Hot_Deals = {
        "1." : "N500- 750MB+N500 Talktime. Val/14days",
        "2." : "N1,000- 1.5GB+N1000 Talktime. Valid 30days",
        "3." : "N2,000- 4.5GB+N2000 Talktime. Val/30days",
        "0." : "Back"
        }
# option (9) from BuyData
Mobile_5G = {
        "1." : "N5,000 for 20GB",
        "2." : "N6,000 for 25GB",
        "3." : "N10,000 for 40GB",
        "4." : "N15,000 for 75GB",
        "5." : "N20,000 for 120GB",
        "6." : "N30,000 for 200GB",
        "7." : "N20,000 for 100GB",
        "0." : "Back"
        }

# option (10) from BuyData
YouTube = {
        "1." : "Weekly Plan",
        "2." : "Monthly Plan",
        "0." : "Back"
        }

# option (11) from BuyData
Manage_Data = {
        "1." : "View Active Data Bundle",
        "2." : "Opt in for Auto renewal",
        "3." : "Cancel Auto renewal",
        "4." : "Deal Zone Offers",
        "0." : "Back"
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