import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read

fname = 'GW_jug_short'
Fs, h = read('%s.wav' % fname)
h = h[2*Fs:]

tc = 15.5 #34.0
t = np.linspace(0, tc, 1000)
Mc = 0.26 #0.17
m1 = Mc * 2**0.2
f = 155.7 / Mc**(5/8.0) / (tc - t)**(3/8.0) * (t < tc)

plt.figure(figsize=(10,4))
plt.specgram(h, Fs=Fs, NFFT=1024, scale_by_freq=True, cmap='plasma')
plt.xlim([0,len(h) / Fs])
plt.ylim([0,2000])
plt.clim([25,50])

plt.plot(t, f, color='lawngreen', ls=':', lw=3, label=r'$m_1=m_2=%.2fM_\odot,\ t_c=%.1fs$' % (m1, tc))
plt.text(1, 250, r'$m_1=m_2=%.2fM_\odot,\ t_c=%.1fs$' % (m1, tc), color='lawngreen', fontsize=15)

'''
plt.plot(t,f * 5.5, color='lawngreen', ls=':', lw=3, label='5.5$f_0$')
plt.text(1, 850, '5.5$f_0$', color='lawngreen', fontsize=15)
plt.plot(t,f * 9.5, color='lawngreen', ls=':', lw=3, label='9.5$f_0$')
plt.text(1, 1400, '9.5$f_0$', color='lawngreen', fontsize=15)
plt.plot(t,f * 13.5, color='lawngreen', ls=':', lw=3, label='13.5$f_0$')
plt.text(1, 1800, '13.5$f_0$', color='lawngreen', fontsize=15)
'''

#plt.legend(loc='upper left', fontsize=13)
#plt.yscale('log')
#plt.colorbar()
plt.xlabel(r'time (s)', fontsize=14)
plt.ylabel(r'frequency (Hz)', fontsize=14)
plt.tight_layout()
plt.savefig('%s_new.png' % fname)
plt.show()
