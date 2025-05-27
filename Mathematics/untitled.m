% Set up vector for zeros
	z = [j ; -j];

	% Set up vector for poles
	p = [-1 ; .5+.5j ; .5-.5j];

	figure(1);
	zplane(z,p);
	title('Pole/Zero Plot for Complex Pole/Zero Plot Example');