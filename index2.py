import colorama
from colorama import Fore, Style
from colorama import TextBlob

colorama.init()

print(f"{Fore.Cyan} Welcome to Sentiment Spy, Agent {Style.Reset_all}")

user_name = input(f"{Fore.Blue} Enter Your Username: {Style.Reset_all} ").strip()
if not user_name:
    user_name = "Mystery Agent"

conversation_history = []

print(f"\n{Fore.Magenta} Hello Agent, {user_name}!")
print(f"\n{Fore.LIGHTGREEN_EX} Give me a sentence and i will show you and sentiment of it")
print(f"Type {Fore.Yellow}'reset', {Fore.Cyan} 'history', or {Fore.Green} 'exit'{Fore.Blue}To quit.{Style.RESET_ALL}\n")

while True:

    user_input = f"{Fore.Green}>> {Style.RESET_ALL}\n"
    if not user_input:
        print(f"{Fore.Red} Please enter some valid text for it to function{Style.Reset_All}")

    elif user_input.lower() == "Exit":
        print(f"{Fore.Red} Goodbye Agent {user_name}.{Style.Reset_ALL}")

    elif user_input.lower() == 'History':
        if not conversation_history:
            print(f"{Fore.Orange} No history yet...{Style.Reset_ALL}")
        else:
            print(f"{Fore.Skyblue}📃Conversation History: {Style.Reset_ALL}")
            for idx, (text, polarity, sentiment_type) in enumerate(conversation_history, start=1):
                if sentiment_type == "Positive":
                    color = Fore.GREEN
                    emoji = "😊"
                elif sentiment_type == "Negative":
                    color = Fore.RED
                    emoji = "😐"
                else:
                    color = Fore.YELLOW
                    emoji = "😓"

                print(f" {idx}. {color}{emoji} {text}" f"(Polarity: {polarity:.2f}, {sentiment_type}){Style.Reset_ALL}")

    continue

polarity = TextBlob(user_input).sentiment.polarity
if polarity > 0.25:
    sentiment_type == "Positive"
    color = Fore.GREEN
    emoji = "😊"

elif polarity < -0.25:
    sentiment_type == "Negative"
    color = Fore.RED
    emoji = "😐"

else:
    
    sentiment_type == "Neutral"
    color = Fore.YELLOW
    emoji = "😒"