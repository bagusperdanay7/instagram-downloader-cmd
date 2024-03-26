import instaloader
from instaloader import Post, Profile
# Get instance
USER = 'USERNAME-IG'
L = instaloader.Instaloader(
    filename_pattern='{filename}', dirname_pattern='./download/{target}', save_metadata=False, compress_json=False, post_metadata_txt_pattern='')
L.load_session_from_file(USER)


def clean_url_post(url: str):
    """Metode untuk membersihkan url yang tidak bersih
    :param url: url dari post instagram atau reel
    :type url: str """
    url = url.removeprefix("https://www.instagram.com/reel/")
    url = url.removeprefix("https://www.instagram.com/p/")

    substring_border = "/"
    url = url[:url.index(substring_border) + len(substring_border)]
    url = url.removesuffix("/")

    return url


def download_profile_picture():
    """Metode untuk mengunduh Profile Picture dari suatu akun"""
    username_profile = input("Masukkan Username: ")
    profile = Profile.from_username(L.context, username_profile)
    print(f'Mengunduh Avatar {profile.username} ({profile.full_name}) ...')
    L.download_profilepic(profile)


def download_post():
    """Method untuk mengunduh single post saja"""
    input_url = input("Masukkan URL Post: ")
    clean_url = clean_url_post(input_url)

    post = Post.from_shortcode(L.context, clean_url)

    print(
        f'Mengunduh Post: {clean_url} dari {post.owner_username} ...')

    L.download_post(post, target=post.owner_username)


def download_stories_by_profile():
    """Method untuk mengunduh stories dari suatu akun"""
    username = input("Masukkan username: ")
    profile = Profile.from_username(L.context, username)
    print(
        f'Mengunduh Stories dari Profile {profile.username} ({profile.full_name})')
    L.download_profile(profile, download_stories_only=True, profile_pic=False)


def download_highlights_from_username():
    'Method untuk mengunduh highlights dari suatu akun'
    username = input("Masukkan username: ")
    profile = Profile.from_username(L.context, username)
    print(
        f'Mengunduh Highlights dari Profile {profile.username} ({profile.full_name})')
    L.download_highlights(profile.userid)


def download_profile_posts():
    """Method untuk mengunduh"""
    username_profile = input("Masukkan Username: ")
    profile = Profile.from_username(L.context, username_profile)
    print(f'Mengunduh dari Profile {profile.username} ({profile.full_name})')
    L.download_profile(profile, profile_pic=False)


def download_saved_post_self():
    """Metode untuk mengunduh semua saved dari profile (login)"""
    print(f'Mengunduh semua Saved dari {L.context.username}')
    L.download_saved_posts()


while True:
    print("="*20, "MENU DOWNLOAD", "="*20)
    print("0. Keluar Program")
    print("1. Download Avatar")
    print("2. Download Post")
    print("3. Download Stories")
    print("4. Download Highlights")
    print("5. Download All Post from Profile")
    print("6. Download Saved Post (Self)\n")
    option = input("MASUKKAN DOWNLOAD OPTION: ")

    match option:
        case "0":
            print("PROGRAM BERAKHIR!")
            quit()
        case "1":
            print("-"*25)
            print("DOWNLOAD PROFILE PICTURE")
            print("-"*25)
            download_profile_picture()
            print('Download Berhasil!')
        case "2":
            print("-"*25)
            print("DOWNLOAD POST")
            print("-"*25)
            download_post()
            print('Download Berhasil!')
        case "3":
            print("-"*25)
            print("DOWNLOAD STORIES")
            print("-"*25)
            download_stories_by_profile()
            print('Download Berhasil!')
        case "4":
            print("-"*25)
            print("DOWNLOAD HIGHLIGHTS")
            print("-"*25)
            download_highlights_from_username()
            print('Download Berhasil!')
        case "5":
            print("-"*25)
            print("DOWNLOAD PROFILE POSTS")
            print("-"*25)
            download_profile_posts()
            print('Download Berhasil!')
        case "6":
            print("-"*25)
            print("DOWNLOAD SAVED POST")
            print("-"*25)
            download_saved_post_self()
            print('Download Berhasil!')
        case _:
            print("Masukkan Dengan Benar!")

    selesai = input('Apakah Ingin Mengakhiri program? (y/n): ')

    if (selesai == 'y' or selesai == 'Y'):
        break

print("\nProgram Berakhir!")
