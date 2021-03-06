'''
Temp configuration file from learnedWS
'''


import configargparse
from utils.data_utils import loadConfigFile


def get_options(script='config_file', ignore_config=False):
    """
    config parser wrapper. Used to generate options object that can be
    propagated throughout all member classes of the trainer class
    :param options:
    """

    confFile = loadConfigFile("./config/paths.yaml")
    dataPath = confFile['CREMI_data']

    p = configargparse.ArgParser(default_config_files=['./config/%s.conf' %(script)])

    # where to save the net
    def_net_name = 'V5_BN_times100_ft'

    if ignore_config:
        # do not use config specified by -c
        p.add('-c', '--my-config')
    else:
        p.add('-c', '--my-config', is_config_file=True)

    p.add('--net_name', default=def_net_name)
    p.add('--net_arch', default="ID_v5_hydra_BN")
    p.add('--no-save_net', dest='save_net_b', action='store_false')
    p.add('--val_name', default='')     # empty strings have catastrophic consequences!!!!
    p.add('--validation_b', default=False, action='store_true')     # empty strings have catastrophic consequences!!!!

    # reload existing net
    p.add('--load_net', dest='load_net_b', action='store_true')
    p.add('--load_net_path', default='None')
    p.add('--load_init_net_path', default='None')

    p.add('--gpu', default='gpu0')

    # train data paths
    def_train_version = 'second_repr'       # def change me
    p.add('--dataset', default="Polygon")

    p.add('--train_version', default=def_train_version)
    p.add('--seed_method', type=str, default="timo",
          help='available metods: gt, timo, grid',
          dest='seed_method')
    p.add('--s_minsize', type=int, default=0)
    p.add('--input_data_path', type=str, default="None")
    p.add('--all_edges', type=str, default="")

    # valid data paths
    def_valid_version = 'first_repr'
    p.add('--valid_version', default=def_valid_version)
    p.add('--max_processes', default=2, type=int)
    p.add('--max_num_gpus', default=4, type=int)
    p.add('--defect_slices_b', default=False, action='store_true')      # if true defect slices will be excluded

    # training general
    p.add('--no-val', dest='val_b', action='store_false')
    p.add('--export_quick_eval', action='store_true')
    p.add('--save_counter', default=1000, type=int)
    p.add('--observation_counter', default=5, type=int)
    p.add('--dummy_data', dest='dummy_data_b', action='store_true')
    p.add('--global_edge_len', default=300, type=int)
    p.add('--fast_reset', action='store_true')
    p.add('--clip_method', default='clip')      # rescale, exp, clip
    p.add('--claim_aug', default='None')
    p.add('--padding_b', action='store_true')
    p.add('--master_training', action='store_true')
    p.add('--master', action='store_true')
    p.add('--validation_slave', action='store_true')
    p.add('--merge_seeds', dest='merge_seeds', action='store_true')
    p.add('--train_merge', dest='train_merge', action='store_true')
    p.add('--dropout_b', action='store_true', default=False)
    p.add('--bnorm_b', action='store_true', default=False)
    p.add('--weight_by_pathlength_b', action='store_true', default=False)
    p.add('--weight_by_distance_b', action='store_true', default=False)
    p.add('--weight_by_RI_b', action='store_true', default=False)
    p.add('--weight_by_importance', action='store_true', default=False)
    p.add('--fully_conf_valildation_b', action='store_true', default=False)
    p.add('--discount_factor', default=0.4, type=float)
    p.add('--future_discount_factor', default=0.999, type=float)

    # pre-training
    p.add('--pre_train_iter', default=600000, type=int)
    p.add('--regularization', default=10. ** 1, type=float)
    p.add('--network_channels', default=1, type=int)
    p.add('--claim_channels', default=2, type=int)
    p.add('--batch_size', default=16, type=int)
    p.add('--quick_eval', action='store_true')
    p.add('--no-augment_pretraining', dest='augment_pretraining', action='store_false')
    p.add('--create_holes', action='store_true', default=False)


    # RNN
    p.add('--n_recurrent_hidden', default=128, type=int)
    p.add('--feature_map_size_reduction', default=1, type=int)
    p.add('--backtrace_length', default=5, type=int)
    p.add('--n_batch_errors', default=1, type=int)
    p.add('--weight_fct', default="hard", type=str)

    # lesion study
    p.add('--lesion_remove_hidden', action='store_true')

    # fine-tuning
    p.add('--batch_size_ft', default=4, type=int)

    p.add('--no-aug-ft', dest='augment_ft', action='store_false')
    p.add('--optimizer', default="nesterov", type=str)
    p.add('--stochastic_update_b', default=False, action='store_true')
    p.add('--learningrate', default=0.000001, type=float)
    p.add('--lr_decrase', default=0.95, type=float)
    p.add('--lr_decrease_counter', default=100, type=int)


    # experience replay

    p.add('--no_bash_backup', action='store_true')
    p.add('--lowercomplete_e', default=0., type=float)

    p.add('--raw_path', default="None", type=str)
    p.add('--membrane_path', default="None", type=str)
    p.add('--label_path', default="None", type=str)
    p.add('--height_gt_path', default="None", type=str)

    # dataprovider

    # polygon
    p.add('--dashes_on_b', action='store_true')
    p.add('--dash_len', default=5, type=int)
    p.add('--hole_length', default=5, type=int)

    # validation
    p.add('--slices_total', type=int, default=10)
    p.add('--start_slice_z', type=int, default=100)

    p.add('--reset_after_fine_tune', action='store_true')
    p.add('--no-ft', dest='fine_tune_b', action='store_false')
    p.add('--reset-ft', dest='rs_ft', action='store_true')
    p.add('--reset_pretraining', dest='reset_pretraining', action='store_true')
    p.add('--margin', default=0.5, type=float)
    # clip_method="exp20"
    p.add('--exp_bs', default=16, type=int)
    p.add('--exp_ft_bs', default=8, type=int)
    p.add('--exp_warmstart', default=1000, type=int)
    p.add('--exp_acceptance_rate', default=0.1, type=float)
    p.add('--no-exp_height', dest='exp_height', action='store_false')
    p.add('--no-exp_save', dest='exp_save', action='store_false')
    p.add('--exp_mem_size', default=20000, type=int)
    p.add('--exp_load', default="None", type=str)
    p.add('--no-exp_loss', dest='exp_loss', action='store_false')
    p.add('--exp_wlast', default=1., type=float)
    p.add('--max_iter', default=10000000000000, type=int)
    p.add('--scale_height_factor', default=100, type=float)
    p.add('--ahp', dest='add_height_penalty', action='store_true')
    p.add('--max_penalty_pixel', default=3, type=float)



    options = p.parse_args()

    # options.slices = range(2000)
    # options.fc_prec = False
    # options.dp_already_exits = True

    if options.input_data_path == "None":
        options.input_data_path ='%s/data/volumes/%sinput_%s.h5' % (dataPath, options.all_edges, options.train_version)
    if options.raw_path == "None":
        options.raw_path ='%s/data/volumes/raw_%s.h5' % (dataPath, options.train_version)
    if options.membrane_path == "None":
        options.membrane_path ='%s/data/volumes/membranes_%s.h5' % (dataPath, options.train_version)
    if options.label_path == "None":
        options.label_path ='%s/data/volumes/label_%s.h5' % (dataPath, options.train_version)
    if options.height_gt_path == "None":
        options.height_gt_path ='%s/data/volumes/height_%s.h5' % (dataPath, options.train_version)

    options.save_net_path = dataPath + '/data/nets/' + options.net_name + '/'
    print('saving files to ', options.net_name)

    # parse validation config
    if not ignore_config and options.val_name != '':
        options.val_options = get_options(script=options.val_name, ignore_config=True)

    return options


if __name__ == '__main__':
    options = get_options()
    print(options)