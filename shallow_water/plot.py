import matplotlib.pyplot as plt
import numpy as np

files = 50
dimx = 100
dimy = 100

field = np.zeros((dimx, dimy), dtype=np.float64)

plt.ion()

fig = plt.figure()
ax = fig.add_subplot(111)

for ifile in range(files):
    print(ifile+1)

    f = open("Output/h.noemulator." + str(ifile+1), "rb")

    # format of each "record" is
    # n_bytes (int), col[0], col[0], col[1], col[2], ..., col[-2], col[-1], col[-1], n_bytes (int)

    f.seek(4)  # skip first integer
    curfile = np.fromfile(f, dtype=np.float64)

    # sanity check on file size
    assert curfile.size == dimy*(dimx + 3) - 1

    # fill in columns
    for ii in range(dimy):
        field[:, ii] = curfile[ii*(dimx + 3) + 1 : (ii + 1)*(dimx + 3) - 2]

    print("Height", np.sum(field))
    plt.imshow(field)
    plt.colorbar()
    # plt.clim(-1.0, 1.0)
    fig.canvas.draw()
    fig.canvas.flush_events()
    plt.clf()
