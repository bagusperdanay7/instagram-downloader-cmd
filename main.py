import instaloader
from instaloader import Post, Profile
import instaloader.exceptions as Except

# Get instance
USER = 'milkitakid'
L = instaloader.Instaloader(
    filename_pattern='{filename}', dirname_pattern='./download/{target}', save_metadata=False, compress_json=False, post_metadata_txt_pattern='')
L.load_session_from_file(USER)


def clean_url_post(url: str):
    """Metode untuk membersihkan url yang tidak bersih
    :param url: url dari post instagram atau reel
    :type url: str """
    url = url.removeprefix("https://www.instagram.com/reel/")
    url = url.removeprefix("https://www.instagram.com/p/")

    slash_symbol = "/"
    has_slash = slash_symbol in url

    if (has_slash is True):
        url = url[:url.index(slash_symbol) + len(slash_symbol)]
        url = url.removesuffix("/")

    return url


def download_profile_picture():
    """Metode untuk mengunduh Profile Picture dari suatu akun"""
    username_profile = input("Masukkan Username: ")
    try:
        profile = Profile.from_username(L.context, username_profile)
    except Except.ProfileNotExistsException:
        print("USERNAME TIDAK DITEMUKAN!")
        print("Download Gagal!")
    except Except.PrivateProfileNotFollowedException:
        print("Akun Ini Bersifat PRIVATE!, Anda tidak dapat mendownloadnya karena anda TIDAK Mengikuti Akun Ini!")
        print("Download Gagal!")
    else:
        print(f'Mengunduh Avatar {profile.username} ({profile.full_name}) ...')
        L.download_profilepic(profile)
        print('Download Berhasil!')


def download_post():
    """Method untuk mengunduh single post saja"""
    input_url = input("Masukkan URL Post: ")
    clean_url = clean_url_post(input_url)

    try:
        post = Post.from_shortcode(L.context, clean_url)
    except Except.BadResponseException:
        print("Gagal Mengambil Data, URL Mungkin Tidak Ada atau Dihapus!, Periksa Kembali dan Coba Lagi!")
        print("Download Gagal!")
    else:
        print(
            f'Mengunduh Post: {clean_url} dari {post.owner_username} ...')

        L.download_post(post, target=post.owner_username)

        print('Download Berhasil!')


def download_stories_by_profile():
    """Method untuk mengunduh stories dari suatu akun"""
    username = input("Masukkan username: ")

    try:
        profile = Profile.from_username(L.context, username)
    except Except.ProfileNotExistsException:
        print("USERNAME TIDAK DITEMUKAN!")
        print("Download Gagal!")
    else:
        try:
            print(
                f'Mengunduh Stories dari Profile {profile.username} ({profile.full_name})')
            L.download_profile(
                profile, download_stories_only=True, profile_pic=False)
        except Except.PrivateProfileNotFollowedException:
            print("Akun Ini Bersifat PRIVATE!, Anda tidak dapat mendownloadnya karena anda TIDAK Mengikuti Akun Ini!")
            print("Download Gagal!")
        else:
            print('Download Berhasil!')


def download_highlights_from_username():
    'Method untuk mengunduh highlights dari suatu akun'
    username = input("Masukkan username: ")

    try:
        profile = Profile.from_username(L.context, username)
    except Except.ProfileNotExistsException:
        print("USERNAME TIDAK DITEMUKAN!")
        print("Download Gagal!")
    else:
        print(
            f'Mengunduh Highlights dari Profile {profile.username} ({profile.full_name})')
        L.download_highlights(profile.userid)
        print('Download Berhasil!')


def download_profile_posts():
    """Method untuk mengunduh"""
    username_profile = input("Masukkan Username: ")

    try:
        profile = Profile.from_username(L.context, username_profile)
    except Except.ProfileNotExistsException:
        print("USERNAME TIDAK DITEMUKAN!")
        print("Download Gagal!")
    else:
        try:
            print(
                f'Mengunduh dari Profile {profile.username} ({profile.full_name})')
            L.download_profile(profile, profile_pic=False)
        except Except.PrivateProfileNotFollowedException:
            print("Akun Ini Bersifat PRIVATE!, Anda tidak dapat mendownloadnya karena anda TIDAK Mengikuti Akun Ini!")
            print("Download Gagal!")
        else:
            print('Download Berhasil!')


def download_saved_post_self():
    """Metode untuk mengunduh semua saved dari profile (login)"""
    print(f'Mengunduh semua Saved dari {L.context.username}')
    L.download_saved_posts()
    print('Download Berhasil!')


def show_display_menu(menu: str):
    """Hanya metode untuk menampilkan menu"""
    print("-"*25)
    print("DOWNLOAD", menu)
    print("-"*25)


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
            show_display_menu('PROFILE PICTURE')
            download_profile_picture()
        case "2":
            show_display_menu('POST')
            download_post()
        case "3":
            show_display_menu('STORIES')
            download_stories_by_profile()
        case "4":
            show_display_menu('HIGHLIGHTS')
            download_highlights_from_username()
        case "5":
            show_display_menu('PROFILE POSTS')
            download_profile_posts()
        case "6":
            show_display_menu('SAVED POST')
            download_saved_post_self()
        case _:
            print("Masukkan Dengan Benar!")

    selesai = input('Apakah Ingin Mengakhiri program? (y/n): ')

    if (selesai == 'y' or selesai == 'Y'):
        break

print("\nProgram Berakhir!")
