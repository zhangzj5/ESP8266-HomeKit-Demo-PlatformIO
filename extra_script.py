Import("env")
print env.Dump()
env.Replace(UPLOAD_ADDRESS="0x14000",)
