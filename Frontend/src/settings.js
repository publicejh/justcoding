let DEBUG = false;
let AUTH_SERVER_HOST_URL = "http://localhost:8000";
let PLATFORM_SERVER_HOST_URL = "http://localhost:8001";
if (DEBUG) {
    AUTH_SERVER_HOST_URL = "http://localhost:8000";
    PLATFORM_SERVER_HOST_URL = "http://localhost:8000";
}

export { AUTH_SERVER_HOST_URL, PLATFORM_SERVER_HOST_URL };
