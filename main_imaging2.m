%%imaging
path='/Users/wanlinxie/Documents/projects/aisleNet/zxing/python-zxing';
im=imread(strcat(path,'/multiple1.png'));
%h=image(im);
imsz=size(im);

%h=fspecial('motion',50,40);

%imcrop1=im(650:1200,800:1350);
%imcrop1=im;
side = 65;
aa=[];
bb=[];
% r=round((imsz(1)-side)*rand(1))+1
% c=round((imsz(2)-side)*rand(1))+1
% r=1080;
% c=940;
% r=270
% c=820
sz=round(side/30);
h=[1*ones(sz),zeros(sz);zeros(sz),ones(sz)*-1];
h2=-h;
wsz=round(side/20);
        h4=zeros(wsz,wsz);
        for i=1:wsz
            for j=1:wsz
                h4(i,j)=1/4-(i/wsz-1/2)^2+(j/wsz-1/2)^2;
            end
        end
        h4=h4 / sum(sum(h4));
loc=[];        
for r=1:side/2:imsz(1)-side
    for c=1:side/2:imsz(2)-side
        imcrop0=im(r:r+side,c:c+side,:);
        imcrop1=(im(r:r+side,c:c+side,1)+im(r:r+side,c:c+side,2)+im(r:r+side,c:c+side,3)/3);
        imFiltered=imfilter(imcrop1,h);
        imFiltered2=imfilter(imcrop1,h2);
        
        imF=imFiltered+imFiltered2;
        

        %h3=ones(10)*0.01;
        %imF2=imfilter(imF,h4);
        imF2=imF;
        mm = max(max(imF2));
        cc = sum(sum(imF2>max(100,mm/2)))/side/side;
        cc1 = sum(sum(imFiltered>max(100,mm/2)))/side/side;
        cc2 = sum(sum(imFiltered2>max(100,mm/2)))/side/side;

        % imBW
%         imfft2=fft2(double(imcrop1));
%         imfft2_a=imfft2 / imfft2(1,1);
% 
%         a=abs(imfft2_a(1,1:side/2));
%         b=abs(imfft2_a(1:side/2,1)');
        % 
        % nr=floor(imsz(1)/side);
        % nc=floor(imsz(2)/side);
        % for ir=1:nr
        %     for ic=1:nc
        %         
        %         imcrop=im((ir-1)*side+1:r+side,c:c+side)
        %if mean(a(4:8))>0.01 && mean(b(4:8))>0.01
        dd=abs(cc1-cc2)/cc;
        if cc > 0.15 && dd < 0.15
            data=[r,c,cc]
            loc=[loc;data];
        [sum(sum(imF2>100))/side/side,sum(sum(imFiltered>100))/side/side,sum(sum(imFiltered2>100))/side/side]
%         aa=[aa;a];
%         bb=[bb;b];
            imwrite(imcrop0,strcat(path,'\images\code_',num2str(size(loc,1)),'_',num2str(r),'_',num2str(c),'_',num2str(round(cc*100)),'_',num2str(round(dd*100)),'.jpg'));
%          figure
%         subplot(2,2,1);imshow(imcrop0);
%         subplot(2,2,2);imshow(imFiltered);
%         subplot(2,2,3);imshow(imFiltered2);
%         subplot(2,2,4);imshow(imF2); %mesh(log(abs(imfft2_a)));
          debug=1;
        else
           % 'No'
        end

    end 
end
