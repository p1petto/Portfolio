import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.5


Window {
    width: 360
    height: 640
    visible: true
    title: qsTr("Task_for_ListView_Model")
    property int defMargin: 8

    Page{
        id:page
        anchors.fill:parent
        footer: PageFooter {
            onNewMessage: {
                //Append new message
                var newMsg = {};
                newMsg.message = msg;
                newMsg.time = Qt.formatTime(new Date(), "hh:mm");
                my_model.append(newMsg);
            }
        }

        Rectangle{
            anchors.fill:parent
            gradient:Gradient{
                GradientStop{position:0;color:"GreenYellow"}
                GradientStop{position:1;color:"MediumSeaGreen"}
            }

        }

        ListModel{
            id:my_model
            ListElement{ message:"Hello"; time:"11:00"}
        }

        Component{
            id:my_delegate
            MyDelegate{
                message:model.message

                time:model.time

                width:parent.width * 0.85
                height:40
                anchors.horizontalCenter: parent.horizontalCenter

            }


        }

        ListView {
            id:my_list
            anchors.fill:parent
            spacing: 20
            model:my_model
            delegate:my_delegate
        }
    }
}
