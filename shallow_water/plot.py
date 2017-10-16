import matplotlib.pyplot as plt
import numpy as np

files = 50
dimx = 100
dimy = 100

h_field = np.zeros((dimx, dimy), dtype=np.float64)
u_field = np.zeros((dimx, dimy), dtype=np.float64)
v_field = np.zeros((dimx, dimy), dtype=np.float64)

plt.ion()

fig = plt.figure()
ax = fig.add_subplot(111)

for ifile in range(files):
    print(ifile+1)

    f_h = open("Output/h.noemulator." + str(ifile+1), "rb")
    f_u = open("Output/u.noemulator." + str(ifile+1), "rb")
    f_v = open("Output/v.noemulator." + str(ifile+1), "rb")

    # format of each "record" is
    # n_bytes (int), col[0], col[0], col[1], col[2], ..., col[-2], col[-1], col[-1], n_bytes (int)

    f_h.seek(4); f_u.seek(4); f_v.seek(4)  # skip first integer
    curfile_h = np.fromfile(f_h, dtype=np.float64)
    curfile_u = np.fromfile(f_u, dtype=np.float64)
    curfile_v = np.fromfile(f_v, dtype=np.float64)

    # sanity check on file sizes
    assert curfile_h.size == dimy*(dimx + 3) - 1
    assert curfile_u.size == dimy*(dimx + 3) - 1
    assert curfile_v.size == dimy*(dimx + 3) - 1

    # fill in columns
    for ii in range(dimy):
        h_field[:, ii] = curfile_h[ii*(dimx + 3) + 1 : (ii + 1)*(dimx + 3) - 2]
        u_field[:, ii] = curfile_u[ii*(dimx + 3) + 1 : (ii + 1)*(dimx + 3) - 2]
        v_field[:, ii] = curfile_v[ii*(dimx + 3) + 1 : (ii + 1)*(dimx + 3) - 2]

    # TODO: KE = 0.5*h*|u|^2, PE = 0.5*g*h^2
    print("Height", np.sum(h_field))
    plt.imshow(h_field)
    plt.colorbar()
    # plt.clim(-1.0, 1.0)
    fig.canvas.draw()
    fig.canvas.flush_events()
    plt.clf()
