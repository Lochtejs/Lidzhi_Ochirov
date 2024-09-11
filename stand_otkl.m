function S = stand_otkl(x_real, x)
    n = length(x_real);
    S = sqrt(1/(n * (n - 1))*sum((x - x_real).^2));
end