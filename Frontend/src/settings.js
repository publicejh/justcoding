let DEBUG = false;

let AUTH_SERVER_HOST_URL = "http://localhost:8000";
let PLATFORM_SERVER_HOST_URL = "http://localhost:8001";
let CHAT_SERVER_HOST_URL = "http://localhost:8002";
let CHAT_SERVER_SOCKET_URL = "ws://localhost:8002";
let FILE_SERVER_HOST_URL = "http://localhost:8003";

if (DEBUG) {
    AUTH_SERVER_HOST_URL = "http://localhost:8000";
    PLATFORM_SERVER_HOST_URL = "http://localhost:8001";
    CHAT_SERVER_HOST_URL = "http://localhost:8002";
    CHAT_SERVER_SOCKET_URL = "ws://localhost:8002";
    FILE_SERVER_HOST_URL = "http://localhost:8003";
}

export { AUTH_SERVER_HOST_URL, PLATFORM_SERVER_HOST_URL, CHAT_SERVER_HOST_URL, CHAT_SERVER_SOCKET_URL, FILE_SERVER_HOST_URL };
