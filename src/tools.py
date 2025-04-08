import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from agents import function_tool
from dotenv import load_dotenv


load_dotenv()
CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri="http://127.0.0.1:8888/callback",
    scope="user-modify-playback-state user-read-playback-state"
))

@function_tool()
def pause_music():
    """pause now playing music
    """
    print("Pausing playback...")
    
    devices = sp.devices()
    if not devices["devices"]:
        return "no devices found"
    
    device_id = devices["devices"][0]["id"]
    sp.pause_playback(device_id=device_id)
    return f"Playback paused on device: {devices['devices'][0]['name']}"


@function_tool()
def play_music():
    """play music on the current device
    """
    print("Starting playback...")
    
    devices = sp.devices()
    if not devices["devices"]:
        return "no devices found"
    
    device_id = devices["devices"][0]["id"]
    
    sp.start_playback(device_id=device_id)
    return f"Playback started on device: {devices['devices'][0]['name']}"
