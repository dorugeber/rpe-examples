import matplotlib.pyplot as plt
import numpy as np

files = 50
dimx = 100
dimy = 100

field = np.zeros((dimx, dimy), dtype=np.float32)

plt.ion()

fig = plt.figure()
ax = fig.add_subplot(111)

for ifile in range(files):
    print(ifile+1)
    curfile = np.fromfile("Output/h.noemulator." + str(ifile+1), dtype=np.float32)

    # format of each "record" is
    # n_bytes (int), col[0], col[0], col[1], col[2], ..., col[-2], col[-1], col[-1], n_bytes (int)

    # sanity check
    assert curfile.size == dimy*(dimx + 4)

    for ii in range(dimy):
        field[:, ii] = curfile[ii*(dimx + 4) + 2 : (ii + 1)*(dimx + 4) - 2]

    plt.imshow(field)
    plt.colorbar()
    # plt.clim(-1.0, 1.0)
    fig.canvas.draw()
    fig.canvas.flush_events()
    plt.clf()
