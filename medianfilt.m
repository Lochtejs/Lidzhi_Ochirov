function mf = medianfilt(x,N)
    num_of_elem = (N - 1) / 2;
    mf = [];
    for i = num_of_elem
        x_new = [x(0), x, x(length(x))];
    end 
    for i = x_new
        x_filt(i) = median(x_new(i : N + i - 1));
        mf(end + 1) = x_filt(i);
    end    
end