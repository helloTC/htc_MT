function p=htc_permutation(a,b,n,tail,method)
%p=Liu_permutation(a,b,n,tail)
%
%This function is aim to do permutation test among a and b.
%Input    a:matrix a
%         b:matrix b
%         n:permutation numbers
%         tail:'both','left','right'
%
%Attention:the size of a and b is n*1
num_a=length(a);

ab = htc_calpermutation(a,b,method);
if size(a,2)~=1
    a=a';
end
if size(b,2)~=1
    b=b';
end
c=[a;b];
c_out=htc_rand(c,n);
a_rand=c_out(1:num_a,:);
b_rand=c_out(num_a+1:end,:);

rand_ab=htc_calpermutation(a_rand,b_rand,method);

if strcmp(tail,'both')
    m=length(find(abs(rand_ab)>=abs(ab)));
elseif strcmp(tail,'right')
    m=length(find(rand_ab>=ab));
elseif strcmp(tail,'left')
    m=length(find(rand_ab<ab));
else error('tail can only input with ''both'' or ''right'' or ''left''')
end
p=m/n;
end

function out=htc_rand(in,n)
    len=length(in);
    k=zeros(len,n);
    out=zeros(len,n);
    for i=1:n
        k(:,i)=randperm(len);
        out(:,i)=in(k(:,i));
    end
end

function out = htc_calpermutation(a,b,method)
	if strcmp(method,'mean')
		out = mean(a)-mean(b);
	elseif strcmp(method,'std')
		out = std(a)-std(b);
	else out = std(a)./mean(a)-std(b)./mean(b);
	end	
end
