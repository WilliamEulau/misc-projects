%{
DEVELOPER: William Eulau, 2022.
Permission to use the file or any part of it is granted if the author
is given credit.

DESCRIPTION
This script will go through two folders of png-images and compare 
corresponding images with each other, providing the jaccard score (JSC) 
and the Sørensen–Dice coefficient (DSC). 

NOTICE: 
It is important that the images being compared are of the same size, are 
named the same, and that they appear in the same place within the folders 
(i.e., the first image in the reference folder corresponds to the first 
image in the second folder etc.). Further, the two folders should 
contain the same amount of images. 
%}

%% Choosing directories with images to compare.
disp('Choose a folder containg reference images:')
refDir = uigetdir();

disp('Choose a folder containg images to test reference images against:')
testDir = uigetdir();

refFiles = dir(fullfile(refDir,'*.png'));
JSC(length(refFiles)) = 0;
DSC(length(refFiles)) = 0;

%% Performing the comparisons, one image pair at a time.
if ~isempty(refFiles)
    wb = waitbar(0,'please wait...'); 
end

for k = 1:length(refFiles)
    baseFileName = refFiles(k).name;
    
    refFullName = append(refDir,'\',baseFileName);
    testFullName = append(testDir,'\',baseFileName);
    
    
    img = im2double(imread(testFullName));
    testImg = zeros(size(img,1),size(img,2)); 
    lum_thresh = 0.05;
    for i = 1:size(img,1)
        for j = 1:size(img,2)
            if img(i,j) > lum_thresh 
                testImg(i,j) = 1;
            else 
                testImg(i,j) = 0;
            end
        end
    end

    [unit8_img] = imread(refFullName);
    refImg = imbinarize(uint8(unit8_img(:, :, 1)*255));
    testImg = imbinarize(testImg);

    
    JSC(k) = jaccard(refImg,testImg);
    DSC(k) = dice(refImg,testImg);
    
    waitbar(k/length(refFiles),wb,append(string(k),'/',...
        string(length(refFiles)),' image comparisons completed')); 

end
close(wb)

%% Calculating mean value and standard deviation for DSC and JCS. 
JSC_mean = mean(JSC);
JSC_std = std(JSC);

DSC_mean = mean(DSC);
DSC_std = std(DSC);

%% Deleting unnecessary variables.
clearvars -except DSC JSC %DSC_mean DSC_mean DSC_std DSC_std