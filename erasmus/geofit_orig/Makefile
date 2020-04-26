geofit:	geofit_chi_test.f
	f77 geofit_chi_test.f -o geofit

go:	geofit
	rm -f chi_out.txt
	rm -f h2o_ice_model_2_fitb.txt
	./geofit
