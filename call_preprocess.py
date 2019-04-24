import preprocess
input_datadir = './images'
output_datadir = './pre_img'

obj=preprocess.preprocesses(input_datadir,output_datadir)
nrof_images_total,nrof_successfully_aligned=obj.collect_data()
# obj2 = preprocess.to_pgm()



