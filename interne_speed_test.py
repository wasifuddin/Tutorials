# pip install speedtest_cli
import speedtest
st = speedtest.Speedtest()
dn_speed = st.download()/1000000
up_speed = st.upload()/1000000
print(f"Download Speed: {dn_speed} mbps Upload Speed: {up_speed} mbps")