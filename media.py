import asyncio

from winrt.windows.media.control import \
    GlobalSystemMediaTransportControlsSessionManager \
    as MediaManager


async def get_media():

    sessions = await MediaManager.request_async()

    current = sessions.get_current_session()

    if not current:
        return None

    try:

        info = await current.try_get_media_properties_async()

        return {
            "title": info.title,
            "artist": info.artist,
            "album": info.album_title,
            "playing": True
        }

    except Exception as e:

        print(e)

        return None