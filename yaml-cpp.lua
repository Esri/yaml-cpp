project "yaml-cpp"

dofile(_BUILD_DIR .. "/static_library.lua")

configuration { "*" }

uuid "7AFE0D10-6046-4248-AC3C-AA09469A2125"

includedirs {
  "include",
}

files {
  "src/*.h",
  "src/*.cpp"
}

if (_PLATFORM_ANDROID) then
end

if (_PLATFORM_COCOA) then
end

if (_PLATFORM_IOS) then
end

if (_PLATFORM_LINUX) then
end

if (_PLATFORM_MACOS) then
end

if (_PLATFORM_WINDOWS) then
end

if (_PLATFORM_WINUWP) then
end
