import requests
import os
import glob
from PIL import Image
import numpy as np

def getTileByXYZ(xidx,yidx,z,file_path):  # 根据x，y，z参数获取瓦片

    for y in range(yidx[0], yidx[1] + 1):
        for x in range(xidx[0], xidx[1] + 1):
            url = "https://api.map.baidu.com/customimage/tile?&x={x}&y={y}&z={z}&udt=20200928&scale=1&ak=8d6c8b8f3749aed6b1aff3aad6f40e37&styles=t%3Agreen%7Ce%3Ag.f%7Cc%3A%23ccccccff%7Ch%3A%23cccccc%2Ct%3Awater%7Ce%3Aall%7Cc%3A%23bdbdbdff%7Ch%3A%23bdbdbd%2Ct%3Alocal%7Ce%3Aall%7Cv%3Aoff%7Cc%3A%23ccccccff%7Ch%3A%23cccccc%2Ct%3Aroad%7Ce%3Aall%7Cc%3A%23ccccccff%7Ch%3A%23cccccc%2Ct%3Aarterial%7Ce%3Aall%7Cv%3Aoff%2Ct%3Aland%7Ce%3Aall%7Cc%3A%23f0f0f0ff%7Ch%3A%23f0f0f0%2Ct%3Aall%7Ce%3Al%7Cv%3Aoff%2Ct%3Agreen%7Ce%3Aall%7Cv%3Aon".format(
                x=x, y=y, z=z)
            savePngByXYZ(url, x, y,file_path)



def savePngByXYZ(url, x, y,file_path):  # 保存图片
    r = requests.get(url)
    sname = file_path +"cd_{x}_{y}.png".format(x=x, y=y)  # 这里建议保存编码是y_x 这样下面合并图片也要适当改代码
    with open(sname, 'ab') as pngf:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                pngf.write(chunk)
                pngf.flush()

def complieImg(file_path,psave):
    # 命名规则：cd_x_y.png 左下坐标系
    # 同一个x 同1列，y增加，图片在上面
    # 假设输入排好序了
    plst = glob.glob(os.path.join(file_path, '*.png'))

    xmin = ((plst[0].split("\\")[1]).split(".")[0]).split('_')[1]
    print(xmin)
    alst = []  # 3维
    qlst = []
    for f in plst:
        w = ((f.split("\\")[1]).split(".")[0]).split('_')  # ['cd', '22568', '6898']
        w[0] = f
        if w[1] == xmin:
            qlst.append(w.copy())
        else:
            alst.append(qlst.copy())
            xmin = w[1]
            qlst = []
    m2 = [256 * len(alst[0]), 256 * len(alst)]  # im2=Image.new('RGBA', (m2[0], m2[1]))
    print(m2)

    iw = 0
    for k in alst:  # k里面装的是x相同的值，y应该递增
        plen = len(k)
        msize = [256, 256 * (plen + 1)]
        print(msize)
        toImage = Image.new('RGBA', (msize[0], msize[1]))
        for i in range(plen):
            from PIL import ImageFile
            ImageFile.LOAD_TRUNCATED_IMAGES = True
            fromImage = Image.open(k[plen - i - 1][0])
            toImage.paste(fromImage, (0 * msize[0], i * msize[0]))

        sname = "/m_{x}.png".format(x=k[0][1])
        iw += 1

        toImage.save(psave + sname)

def complieImgInY(p_in,p_save,fianl_out):
    # 合并长条形图片，x变化，y不变 长图是complieImg()里生成的

    plst = glob.glob(os.path.join(p_in, '*.png'))

    xmin = ((plst[0].split("\\")[1]).split(".")[0]).split('_')[1]
    ima21 = Image.open(plst[0])
    w = np.array(ima21).shape
    print(w)

    plen = len(plst)
    msize = [w[1] * plen / 2, w[0] / 2]
    print(msize)
    toImage = Image.new('RGBA', (int(msize[0]), int(msize[1])))
    for i in range(plen):
        fromImage = Image.open(plst[i])
        fromImage = fromImage.resize((int(256 / 2), int(msize[1])), Image.ANTIALIAS)
        toImage.paste(fromImage, (int(i * 256 / 2), 0))



    toImage.save(p_save + fianl_out)  # 保存图片

def main():
    z = 15
    xidx = [258, 272]
    yidx = [3331, 3338]
    file_path = "./阿姆斯特丹/"
    p_save = "./complexLevel"
    p_out= "./concat"
    savename = "/amustedanMap.png"
    getTileByXYZ(xidx,yidx,z,file_path)
    complieImg(file_path,p_save)
    complieImgInY(p_save,p_out,savename)


if __name__ == '__main__':
    main()
