let DEBUG = false;
let PLATFORM_SERVER_HOST_URL = "http://localhost:8000";
let CHAT_SERVER_HOST_URL = "http://localhost:8001";
let CHAT_SERVER_SOCKET_URL = "ws://localhost:8001";
if (DEBUG) {
  PLATFORM_SERVER_HOST_URL = "http://localhost:8000";
  CHAT_SERVER_HOST_URL = "http://localhost:8001";
  CHAT_SERVER_SOCKET_URL = "ws://localhost:8001";
}

export { CHAT_SERVER_HOST_URL, CHAT_SERVER_SOCKET_URL };