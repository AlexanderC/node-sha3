{
  "targets": [
    {
      "target_name": "sha3",
      "sources": [
        "src/addon.cpp",
        "src/displayIntermediateValues.cpp",
        "src/KeccakF-1600-reference.cpp",
        "src/KeccakNISTInterface.cpp",
        "src/KeccakSponge.cpp"
      ],
      "xcode_settings": {
        "MACOSX_DEPLOYMENT_TARGET": "10.7",

        "OTHER_CFLAGS": [
          "-std=c++11",
          "-stdlib=libc++"
        ],
      },
      "include_dirs": [
          "<!(node -e \"require('nan')\")"
      ]
    }
  ]
}
