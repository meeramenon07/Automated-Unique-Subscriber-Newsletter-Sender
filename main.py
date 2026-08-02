# Initialize an empty set for subscribers
# Initialize an empty set for subscribers
my_subs = set()


def add_sub(email_id):
    """Adds a new email to the subscriber set."""
    
    clean_email_id = email_id.strip().lower()

    if clean_email_id in my_subs:
        print(f"DUPLICATE email! {clean_email_id} is already subscribed.")
    else:
        my_subs.add(clean_email_id)
        print(f"SUCCESS! Subscribed: {clean_email_id}")


def send_newsletter(topic, content):
    """sending a newsletter to all unique subscribers."""
    print(f"\n--- Sending Weekly My Newsletter Tutorial: '{topic}' ---")
    if not my_subs:
        print("No subscribers found.")
        return

    for email_id in my_subs:
        print(f"Sending weekly email to: {email_id}")
    print(f"Done! Email Sent to {len(my_subs)} unique subscriber(s).\n")


# --- Demonstration ---

# 1. Adding subscribers (including duplicate)
add_sub("ann@yahoo.com")
add_sub("ben@yahoo.com")
add_sub("Ann@yahoo.com")  
add_sub("ann@yahoo.com")  
add_sub("tom@yahoo.com")

# 2. View active subscriber list count
print(f"\nMy Total Unique Subscribers Are : {len(my_subs)}")

# 3. Send out newsletter batch
send_newsletter(
    "Weekly Python Tips", "Here is your weekly breakdown of Python sets!"
)
