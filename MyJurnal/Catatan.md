TODO:
	- Update Proses Repair (done)
		Note: from jurnal 2023_12_29
			"Jadi mungkin nanti pas repair (atau mutation) dia bakal assign jadwal dengan secara random milih dari jadwal tersedia si partisipant aja kali ya (dari pada secara random generate si jadwal sampe ngga ada konflik, gw make ini soalnya asumsi kalo ada konflik dikit gapapa, tapi kalo gitu apa gunanya sistem ini), terus cek juga apakah itu konflik sama jadwal si aslab, kalo ngga ada maka dia di assign ke aslab baru. "
			
	- Implementasi NGSA-2
		Note: from jurnal 2023_12_29
			"Gw udah nonton baca dikit (nanya chat gpt hmm) dan nonton youtube dikit, simpelnya kalo ada multi objektif (berbagai tujuan yang berbeda, atau fungsi fitness yang beda), maka cocok make algoritma ini, jadi mungkin bisa gw terapin algoritma-nya."
			"Ada Non-Dominated Sorting dan Crowding Distance Sorting, keduanya cuman mekanisme mengurutkan chromosome, jadi keknya ngga terlalu drastis banget hal yang mesti gw rubah."
			
	- Implementasi Tabu Search (done, tapi malah bikin bottleneck)
	- Implementasi local search lain.
		Note: "Udah nyoba simulated annealing, lumayan sih, sedikit lebih cepet dari tabu search."
	
	- Implementasi adaptive crossover dan mutation rate, berdasarkan diversity.
	- Nyoba struktur data baru, tapi setelah nyoba local search lain.
	
	- Bikin regenerasi jadwal lebih terpusat, fokus maksimalin shift buat nampung beberapa grup sekaligus.
	
	- Jadiin preferensi jadwal si asisten jadi pertimbangan juga. (Bisa ditaro di constraint terus di panggil pas proses repair, atau pass fungsi fitness sih)