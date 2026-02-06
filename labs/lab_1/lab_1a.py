"""
lab_1a.py

The first lab in the BWSI CSS course. To complete this lab, fill out the variable on line 10
with your name. Then, save the code, add it to the staging area, and commit it to the Git tree.
"""

def main():
    print("Hello World!")

    name = "Kuan Dai"

    print(f"{name}, Welcome to the CSS course!")

    print("""Hello everyone, my name is Kuan Dai and I am a high school sophomore located in Washington. I enjoy small scale electronics projects (ESPHome trinkets, mesh RF, and a remote control RC car I built), maintaining and expanding my homelab infrastructure, and programming in my free time! I've also been playing with FPV lately, although only at the simulator level so far. I have experience in C++ and Java, and am currently dabbling in some Rust.

I find it to be quite relaxing and empowering to deploy my own selfhosted services, rather than using large corporate solutions. I maintain a Nextcloud instance for my family and friends, as well as email, Jellyfin, and an OIDC provider to string it all together. I'm currently working on a PKI-based authentication system in C++ for my Minecraft clone.

Looking forwards to getting to know everybody better.""")

if __name__ == "__main__":
    main()
