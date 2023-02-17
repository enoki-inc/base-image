instructions to build the image:

sudo docker build -t enoki-base -f Dockerfile .

sudo docker run --name u-test \
--privileged \
-e XDG_RUNTIME_DIR=/home/dev \
-e WAYLAND_DISPLAY=$WAYLAND_DISPLAY \
-e WLR_BACKENDS=headless \
-e WLR_LIBINPUT_NO_DEVICES=1 \
-e --user=dev \
-v /var/run/docker.sock:/var/run/docker.sock \
-v $XDG_RUNTIME_DIR/$WAYLAND_DISPLAY:/home/1000/$WAYLAND_DISPLAY \
-p 6080:6080 \
-p 6081:6081 \
-p 6082:6082 \
-p 6083:6083 \
-p 6084:6084 \
-p 6085:6085 \
-p 6086:6086 \
-p 6087:6087 \
-p 6088:6088 \
-p 6089:6089 \
-p 6090:6090 \
--rm  enoki-base dbus-run-session -- sway
