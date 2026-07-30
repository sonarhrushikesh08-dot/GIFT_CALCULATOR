# ==============================================================
# Project  : GIFT (DAHEJ) CALCULATOR (Satirical)
# Author   : Hrushikesh Sonar
# Language : Python
#
# Description:
# This project is a humorous satire on the dowry system.
# It presents exaggerated stereotypes in a terminal-based
# "billing system" style to encourage reflection.
#
# Final Result:
# No matter what options are selected, the program concludes
# that dowry is illegal and unethical and that the only
# acceptable dowry is ₹0.
# ==============================================================

greed_score = 0
receipt = []

print("=" * 70)
print("😂 WELCOME TO THE GIFT (DAHEJ) CALCULATOR 😂".center(70))
print("=" * 70)

print(f"""
⚠️  WARNING

This software may hurt the feelings of:

✔️ Greedy uncles
✔️ "Government job = jackpot" believers
✔️ "Hamare bete ke liye line lagi hai" families
✔️ Self-proclaimed Kings 👑 and Sigma Males 🐺

😌 Normal people have nothing to worry about.

📜 This program is purely satirical and does NOT promote
   or encourage the practice of dowry in any form.

❤️ The only acceptable dowry is ₹0.

Proceed only if your sense of humour is installed. 😄
""")

print("=" * 65)
print("😂 WELCOME TO THE GIFT (DAHEJ) CALCULATOR 😂".center(65))
print("=" * 65)

print("⚠️  YEH SIRF SAMAJ KO AAINA DIKHANE KE LIYE HAI.")
print("⚠️  KRIPYA DIL AUR FEFDON PAR NA LEIN.")
print("=" * 65)

while True:

    greed_score = 0
    receipt.clear()

    print("\nStarting New Analysis...")
    print("-" * 65)

    # ===========================
    # GROOM INFORMATION DATABASE
    # ===========================

    profile = {}

    # -----------------
    # Groom Profession
    # ------------------

    print("\n" + "=" * 60)
    print("👨 GROOM PROFESSION".center(60))
    print("=" * 60)

    print("1. 👮 Government Job")
    print("2. 💼 Private Job")
    print("3. 🏪 Businessman")
    print("4. 🚀 Entrepreneur")
    print("5. 📚 Preparing for Govt Exams")

    choice = input("\nEnter Choice : ")

    profession = {
        "1": "Government Job",
        "2": "Private Job",
        "3": "Businessman",
        "4": "Entrepreneur",
        "5": "Preparing for Govt Exams"
    }

    profile["Profession"] = profession.get(choice, "Not Specified")

    print(f"✔ Selected : {profile['Profession']}")


    # ---------------
    # Family Details
    # ---------------

    print("\n" + "=" * 60)
    print("👨‍👩‍👧‍👦 FAMILY DETAILS".center(60))
    print("=" * 60)

    print("1. Joint Family")
    print("2. Nuclear Family")

    choice = input("\nEnter Choice : ")

    family = {
        "1": "Joint Family",
        "2": "Nuclear Family"
    }

    profile["Family Type"] = family.get(choice, "Not Specified")

    print(f"✔ Selected : {profile['Family Type']}")


    # ------------------
    # Agricultural Land
    # ------------------
    print("\n" + "=" * 60)
    print("🚜 AGRICULTURAL LAND".center(60))
    print("=" * 60)

    print("1. No Land")
    print("2. Less than 5 Acres")
    print("3. 5 - 20 Acres")
    print("4. More than 20 Acres")

    choice = input("\nEnter Choice : ")

    land = {
        "1": "No Land",
        "2": "Less than 5 Acres",
        "3": "5 - 20 Acres",
        "4": "More than 20 Acres"
    }

    profile["Land"] = land.get(choice, "Not Specified")

    print(f"✔ Selected : {profile['Land']}")


    # ---------------
    # Family Business
    # ---------------

    print("\n" + "=" * 60)
    print("🏪 FAMILY BUSINESS".center(60))
    print("=" * 60)

    print("1. None")
    print("2. Kirana Shop")
    print("3. Medium Business")
    print("4. Large Business")

    choice = input("\nEnter Choice : ")

    business = {
        "1": "None",
        "2": "Kirana Shop",
        "3": "Medium Business",
        "4": "Large Business"
    }

    profile["Business"] = business.get(choice, "Not Specified")

    print(f"✔ Selected : {profile['Business']}")


    # -------
    # Vehicle
    # --------
    print("\n" + "=" * 60)
    print("🚗 VEHICLE".center(60))
    print("=" * 60)

    print("1. Bicycle")
    print("2. Splendor")
    print("3. Bullet")
    print("4. Thar")
    print("5. Fortuner")

    choice = input("\nEnter Choice : ")

    vehicle = {
        "1": "Bicycle",
        "2": "Splendor",
        "3": "Bullet",
        "4": "Thar",
        "5": "Fortuner"
    }

    profile["Vehicle"] = vehicle.get(choice, "Not Specified")

    print(f"✔ Selected : {profile['Vehicle']}")


    # --------------
    # Qualification
    # --------------

    print("\n" + "=" * 60)
    print("🎓 QUALIFICATION".center(60))
    print("=" * 60)

    print("1. 10th Pass")
    print("2. Graduate")
    print("3. Engineer")
    print("4. Doctor")
    print("5. IAS / IPS")

    choice = input("\nEnter Choice : ")

    qualification = {
        "1": "10th Pass",
        "2": "Graduate",
        "3": "Engineer",
        "4": "Doctor",
        "5": "IAS / IPS"
    }

    profile["Qualification"] = qualification.get(choice, "Not Specified")

    print(f"✔ Selected : {profile['Qualification']}")


    # ----------
    # Residence
    # ----------
    print("\n" + "=" * 60)
    print("🌍 RESIDENCE".center(60))
    print("=" * 60)

    print("1. Village")
    print("2. City")
    print("3. Metro City")
    print("4. Abroad")

    choice = input("\nEnter Choice : ")

    residence = {
        "1": "Village",
        "2": "City",
        "3": "Metro City",
        "4": "Abroad"
    }

    profile["Residence"] = residence.get(choice, "Not Specified")

    print(f"✔ Selected : {profile['Residence']}")


    # --------------
    # Instagram Bio
    # --------------
    print("\n" + "=" * 60)
    print("📱 INSTAGRAM BIO".center(60))
    print("=" * 60)

    print("1. Simple Boy ❤️")
    print("2. King 👑")
    print("3. Sigma Male 🐺")
    print("4. Attitude 😎")
    print("5. No Instagram")

    choice = input("\nEnter Choice : ")

    bio = {
        "1": "Simple Boy",
        "2": "King",
        "3": "Sigma Male",
        "4": "Attitude",
        "5": "No Instagram"
    }

    profile["Instagram Bio"] = bio.get(choice, "Not Specified")

    print(f"✔ Selected : {profile['Instagram Bio']}")


    # ----------------------
    # Government Exam Status
    # -----------------------
    print("\n" + "=" * 60)
    print("📚 GOVERNMENT EXAM STATUS".center(60))
    print("=" * 60)

    print("1. Cleared")
    print("2. Preparing")
    print("3. Not Interested")

    choice = input("\nEnter Choice : ")

    exam = {
        "1": "Cleared",
        "2": "Preparing",
        "3": "Not Interested"
    }

    profile["Government Exam"] = exam.get(choice, "Not Specified")

    print(f"✔ Selected : {profile['Government Exam']}")


    # ------------------------------
    # Mother's Dialogue
    # ------------------------------

    print("\n" + "=" * 60)
    print("               😄 MOTHER'S DIALOGUE")
    print("=" * 60)

    print("1. Hamare bete ke liye line lagi hai.")
    print("2. Bas achhi bahu chahiye.")
    print("3. Hume kuch nahi chahiye.")
    print("4. Sab Bhagwan ki kripa hai.")

    choice = input("\nEnter Choice : ")

    dialogue = {
        "1": "Hamare bete ke liye line lagi hai.",
        "2": "Bas achhi bahu chahiye.",
        "3": "Hume kuch nahi chahiye.",
        "4": "Sab Bhagwan ki kripa hai."
    }

    profile["Mother's Dialogue"] = dialogue.get(choice, "Not Specified")

    print(f"✔ Selected : {profile["Mother's Dialogue"]}")
    

    # ----------
    # Ego Level
    # -----------
    print("\n" + "=" * 60)
    print("😎 EGO LEVEL".center(60))
    print("=" * 60)

    print("1. Humble")
    print("2. Confident")
    print("3. Overconfident")
    print("4. Walking Red Flag")

    choice = input("\nEnter Choice : ")

    ego = {
        "1": "Humble",
        "2": "Confident",
        "3": "Overconfident",
        "4": "Walking Red Flag"
    }

    profile["Ego Level"] = ego.get(choice, "Not Specified")

    print(f"✔ Selected : {profile['Ego Level']}")


    # ----------------
    # Special Demands
    # -----------------

    print("\n" + "=" * 60)
    print("🎁 SPECIAL DEMANDS".center(60))
    print("=" * 60)

    print("1. None")
    print("2. Destination Wedding")
    print("3. Luxury Wedding")
    print("4. Grand Reception")

    choice = input("\nEnter Choice : ")

    demand = {
        "1": "None",
        "2": "Destination Wedding",
        "3": "Luxury Wedding",
        "4": "Grand Reception"
    }

    profile["Special Demand"] = demand.get(choice, "Not Specified")

    print(f"✔ Selected : {profile['Special Demand']}")


    print("\n")
    print("=" * 60)
    print("PROFILE SUMMARY".center(60))
    print("=" * 60)

    for key, value in profile.items():
        print(f"{key:<25}: {value}")

    print("=" * 60)
    # --------
    # Receipt
    # ---------
    print("\n")
    print("=" * 65)
    print("GREED RECEIPT".center(65))
    print("=" * 65)

    if len(receipt) == 0:
        print("No selections recorded.")

    else:
        print(f"{'Category':<40}{'Score':>10}")
        print("-" * 65)

        for category, score in receipt:
            print(f"{category:<40}+{score}")

    print("-" * 65)
    print(f"{'TOTAL GREED SCORE':<40}{greed_score}")

    # --------
    # Verdict
    # ---------

    print("\n")

    if greed_score <= 150:
        print("😊 Verdict : Green Flag")

    elif greed_score <= 350:
        print("🙂 Verdict : Thoda Sambhal Jao")

    elif greed_score <= 600:
        print("🤨 Verdict : Shaadi Ya Deal?")

    elif greed_score <= 850:
        print("🚩 Verdict : Walking Red Flag")

    else:
        print("💀 Verdict : Gift Premium Plus Ultra Max Family")

    # ---------------
    # Final Message
    # ---------------
    print("\n")
    print("=" * 65)
    print("FINAL RESULT".center(65))
    print("=" * 65)

    print("❌ ERROR 404 : Humanity Not Found\n")

    print("Processing Dowry Request...")
    print("████████████████████ 100%\n")

    print("Deleting Greed...")
    print("████████████████████ 100%\n")

    print("Final Greed Score : 0\n")

    print("❌ ERROR : Dowry is illegal and unethical.")
    print("💡 Marriage is a partnership, not a transaction.")
    print("📜 Dowry Prohibition Act, 1961")
    print("❤️ Respect > Money")
    print("🤝 Equality > Status")
    print("\nAcceptable Dowry : ₹0")

    print("=" * 65)

    again = input("\nDo you want to analyse another family? (Yes/No): ").strip().lower()

    if again != "yes":
        print("\nThank you for supporting a dowry-free society. ❤️")
        break