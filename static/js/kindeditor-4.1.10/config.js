/**
 * Created by tarena on 18-11-1.
 */
KindEditor.ready(function(K) {
        window.editor = K.create(
            'textarea[name=content]',{
            width:'800px',
            height:'200px',
            uploadJson: '/admin/upload/kindeditor',
        });
});